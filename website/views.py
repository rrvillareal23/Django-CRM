from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record, Installer
from .filters import OrderFilter

from .decorators import allowed_user

#login info     Employee Login        Insatller         Admin
#admin          Tester                Trout             TestAdmin
#password       testing123!           Zxcvbnm,./        Zxcvbnm,./

def home(request):
    records = Record.objects.all()
    installers = Installer.objects.all()
    
    myFilter = OrderFilter(request.GET, queryset=records)
    records = myFilter.qs
    
    waiting_on_tou = records.filter(project_status='Waiting on Tou').count()
    waiting_on_survey = records.filter(project_status='Waiting on Survey').count()
    waiting_on_deposit = records.filter(project_status='Waiting on Deposit').count()
    waiting_on_installer = records.filter(project_status='Waiting on Installer').count()
    waiting_on_customer = records.filter(project_status='Waiting on Customer').count()
    waiting_on_appointment = records.filter(project_status='Waiting on Appointment').count()
    waiting_on_permit = records.filter(project_status='Waiting on Permit').count()
    waiting_on_install = records.filter(project_status='Waiting on Install').count()
    install_completed = records.filter(project_status='Install Completed').count()

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
        'myFilter': myFilter
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
    