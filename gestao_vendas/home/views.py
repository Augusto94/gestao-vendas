from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    log_out(request)
    return redirect('home')