"""Remkay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
#create your tests here
app_name = "userapp"

urlpatterns = [
    path("", Home, name = "homepage"),
    path("blog",Blog, name ="student"),
    path("payment_status",UserPayment, name ="student"),
    path("about", UserAbout, name="about"),
    path("privacy", Privacy, name="privacy"),
    path("contact",UserContact, name ="student"),
    path('userapp/', include('django.contrib.auth.urls')),
    path('users/userfeedbackform', Userfeedback, name = "userfeedform"),
    path('userapp/signup',SignUp, name= "signup"),
    path('userapp/userlogout',UserLogout, name= "userlogout"),
    path('makepayments',MakePayments, name= "payments"),
    path('uploadconfirmation',ConfirmUpload, name= "uploadconfirmation"),
    path('successfulpayment',PaymentSuccessful, name= "successfulpayment"),
    path('allpayment',AllPayments, name= "allpayment"),
]