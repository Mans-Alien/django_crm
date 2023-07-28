from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
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
        return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "logout...")
    return redirect("home")