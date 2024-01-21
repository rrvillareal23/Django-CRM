from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record, Installer

from .decorators import allowed_user

#login info     Employee Login        Insatller         Admin
#admin          Tester                Trout             TestAdmin
#password       testing123!           Zxcvbnm,./        Zxcvbnm,./

def home(request):
    records = Record.objects.all()
    installers = Installer.objects.all()
    
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
            messages.warning(request, "Error logging in, please try again...", extra_tags="warning")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records, 'installers':installers})
        

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