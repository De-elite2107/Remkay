from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from payments.models import UserWallet
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create(username=username, password=password)
        UserWallet.objects.create(user=user)
        return redirect('/accounts/login')
    return render(request, "paystack/register.html")

def login_view(request):    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/payments/initiate_payment')
        else:
            return redirect('/accounts/login')

    return render(request, 'paystack/login.html')

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('login')