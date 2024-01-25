from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record, Installer

from django.db.models import Q

from .decorators import allowed_user

#login info     Employee Login        Insatller         Admin
#admin          Tester                Trout             TestAdmin
#password       testing123!           Zxcvbnm,./        Zxcvbnm,./

def home(request):
    q = request.GET.get('q', '')
    installers = Installer.objects.all()
   
    if q:
        # Check if the query is a number
        if q.isdigit():
            records = Record.objects.filter(id=q)
        else:
            # Split the query into words
            words = q.split()

            # Check if there are two words in the query
            if len(words) == 2:
                first_name, last_name = words
                records = Record.objects.filter(Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name))
            else:
                records = Record.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
    else:
        records = Record.objects.all()

    sort_by = request.GET.get('sort_by', 'id')  # Default to sorting by ID
    records = records.order_by(sort_by)


    waiting_on_tou = records.filter(project_status='Waiting on Tou').count()
    waiting_on_survey = records.filter(project_status='Waiting on Survey').count()
    waiting_on_deposit = records.filter(project_status='Waiting on Deposit').count()
    waiting_on_installer = records.filter(project_status='Waiting on Installer').count()
    waiting_on_customer = records.filter(project_status='Waiting on Customer').count()
    waiting_on_appointment = records.filter(project_status='Waiting on Appointment').count()
    waiting_on_permit = records.filter(project_status='Waiting on Permit').count()
    waiting_on_install = records.filter(project_status='Waiting on Install').count()
    install_completed = records.filter(project_status='Install Completed').count()
    
    status_content_pairs = [
        ('Waiting on TOUs', waiting_on_tou),
        ('Waiting on Survey', waiting_on_survey),
        ('Waiting on Deposit', waiting_on_deposit),
        ('Waiting on Installer', waiting_on_installer),
        ('Waiting on Customer', waiting_on_customer),
        ('Waiting on Appointment', waiting_on_appointment),
        ('Waiting on Permit', waiting_on_permit),
        ('Waiting on Install', waiting_on_install),
        ('Install Completed', install_completed),
    ]


    context = {
        'records': records, 
        'installers': installers,
        'waiting_on_tou': waiting_on_tou,
        'waiting_on_survey': waiting_on_survey,
        'waiting_on_deposit': waiting_on_deposit,
        'waiting_on_installer': waiting_on_installer,
        'waiting_on_customer': waiting_on_customer,
        'waiting_on_appointment': waiting_on_appointment,
        'waiting_on_permit': waiting_on_permit,
        'waiting_on_install': waiting_on_install,
        'install_completed': install_completed,
        'status_content_pairs': status_content_pairs,
        'search_query': q,  # Include search query in the context
        'sort_by': sort_by,

    }
                
    #check to see if loggin in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!", extra_tags='success')
            return redirect('home')
        else:
            messages.warning(request, "Error logging in, please try again...", extra_tags="danger")
            return redirect('home')
    else:
        return render(request, 'home.html', context)

def installer_dashboard(request):
    return render(request,'installer_dashboard.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...", extra_tags='success')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(user=username, password=password)
            login(request,user)
            messages.success(request, "You have Successfully Registered. Welcome!", extra_tags='success')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        #Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to see that record!", extra_tags='success')
        return redirect('home')

@allowed_user(allowed_roles=['Admin'])    
def delete_record(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            delete_it = Record.objects.get(id=pk)
            delete_it.delete()
            messages.success(request, "Record deleted successfully...", extra_tags='success')
            return redirect('home')
    else:
        messages.success(request, "You must be logged in to Delete a Record!", extra_tags='danger')
        return redirect('home')
    
@allowed_user(allowed_roles=['Admin'])
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == "POST":
                if form.is_valid():
                    add_record = form.save()
                    messages.success(request, "Record Added...", extra_tags='success')
                    return redirect('home')
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged into add record!", extra_tags='warning')

@allowed_user(allowed_roles=['Admin'])
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!", extra_tags='success')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to Delete a Record!", extra_tags='warning')
        return redirect('home')
    