from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()


    #check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "Succesfully logged in")
            return redirect("home")

        else:
            messages.success(request, "error, please make sure of the username and password and try again")
            return redirect("home")
    else:
        return render(request, "home.html", {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "logout...")
    return redirect("home")



def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            #authenticat and login
            username  = form.cleaned_data["username"]
            password  = form.cleaned_data["password1"]
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "your email is successfully created")
            return redirect("home")
        
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form' : form})
    
    return render(request, "register.html", {'form' : form})


def cutomer_record(request, pk):
    if request.user.is_authenticated:
        cutomer_record = Record.objects.get(id = pk)
        return render(request, "record.html", {'cutomer_record' : cutomer_record})
    else:
        messages.success(request, "you need to login first....")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id = pk)
        record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect("home")
    else:
        messages.success(request, "you need to login first....")
        return redirect("home")



@login_required
def add_record(request):
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Added successfully")
            return redirect("home")

    else:
        form = AddRecordForm()
        return render(request, 'add_record.html', {'form':form})