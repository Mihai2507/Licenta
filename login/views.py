from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Date invalide!")

    return render(request, 'login.html')

def user_logout(request):
    if request.method in ["POST", "GET"]:
        logout(request)
    return redirect('home')
