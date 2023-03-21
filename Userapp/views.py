from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import *
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.conf import settings

# Create your views here.
def Userfeedback(request):
    if request.method == "POST":
        form = UserfeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/users/userfeedbacksviews")
    form =  UserfeedbackForm()
    data = {"forms" : form}
    return render(request, "usermessage.html", data)

def SignUp(request):
    myform = UserCreationForm(request.POST or None)
    if(request.method == "POST"):
        if myform.is_valid():
            user = myform.save()
            login(request, user)
            return redirect("/")
    data = {"forms": myform, "title": "User Registration"}
    return render(request, "registration/signup.html", data)

def Homepage(request):
    data = {}
    return render (request,"registration/homepage.html", data)

def UserLogout(request):
    txt = "You have logged Out"
    data = {"text":txt}
    return render(request, "registration/logout.html" , data)

def Home(request):
    data = {}
    return render(request, "home.html", data)

def Blog(request):
    from .models import Blog
    blog = BlogForm()
    posts = Blog.objects.all()
    if request.method == "POST":
        blogs = BlogForm(request.POST, request.FILES or None)
        if blogs.is_valid():
            blogs.save()
    data = {"blog": blog, "posts" : posts}
    return render(request, "blog.html", data)

def UserPayment(request):
    user = request.user
    if user.is_authenticated:
        TotalPay = 0
        TotalBal = 0
        payment = UserPaymentConfirmUpload.objects.filter(USERNAME = request.user)
        for x in payment:
            y = x.AMOUNTPAID
            TotalPay = TotalPay + y
        for x in payment:
            y = x.BALANCE
            TotalBal = TotalBal + y
        data = {"payment": payment, "TotalPay" : TotalPay, "TotalBal" : TotalBal}
        return render(request, "payment_details.html", data)
    else:
        return redirect("/userapp/login")

def MakePayments(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "make_payments.html")
    else:
        return redirect("/userapp/login")

def ConfirmUpload(request):
    initdata={"USERNAME" : request.user, "BALANCE" : 0}
    form = UploadConfirmationForm(initial=initdata)
    if request.method == "POST":
        form=UploadConfirmationForm(request.POST, request.FILES or None)
        if form.is_valid():
            T = form.save(commit = False)
            X = T.AMOUNTPAID
            Y = T.CLASS
            if Y == "KG":
                EXP_AMOUNT = 13000
                BLC=EXP_AMOUNT-X
            if Y == "Prep":
                EXP_AMOUNT = 12000
                BLC=EXP_AMOUNT-X
            if Y == "Nur_1":
                EXP_AMOUNT = 15000
                BLC=EXP_AMOUNT-X
            if Y == "Nur_2":
                EXP_AMOUNT = 15000
                BLC=EXP_AMOUNT-X
            if Y == "B_1":
                EXP_AMOUNT = 16000
                BLC=EXP_AMOUNT-X
            if Y == "B_2":
                EXP_AMOUNT = 16000
                BLC=EXP_AMOUNT-X
            if Y == "B_3":
                EXP_AMOUNT = 16000
                BLC=EXP_AMOUNT-X
            if Y == "B_4":
                EXP_AMOUNT = 17000
                BLC=EXP_AMOUNT-X
            if Y == "B_5":
                EXP_AMOUNT = 17000
                BLC=EXP_AMOUNT-X
            if Y == "Jss_1":
                EXP_AMOUNT = 22500
                BLC=EXP_AMOUNT-X
            if Y == "Jss_2":
                EXP_AMOUNT = 22500
                BLC=EXP_AMOUNT-X
            if Y == "Jss_3":
                EXP_AMOUNT = 22500
                BLC=EXP_AMOUNT-X
            if Y == "Sss_1":
                EXP_AMOUNT = 25000
                BLC=EXP_AMOUNT-X
                EXP_AMOUNT = BLC
            T.BALANCE = BLC
            T.save()
            mod = UserPaymentConfirmUpload.objects.all()
            for x in mod:
                newbalance = x.BALANCE
                newbalance = EXP_AMOUNT
            print(x.BALANCE)
            return redirect("/successfulpayment")
    data = {"form": form}
    return render (request, "upload.html", data)

def PaymentSuccessful(request):
    response = UserPaymentConfirmUpload.objects.filter(USERNAME = request.user)
    data = {"response" : response} 
    return render(request, "succesful_payment.html", data)

def AllPayments(request):
    TotalAmount = 0
    TotalBlc = 0
    allpayment = UserPaymentConfirmUpload.objects.all()
    for x in allpayment:
        y = x.AMOUNTPAID
        TotalAmount = TotalAmount + y
    for x in allpayment:
        y = x.BALANCE
        TotalBlc = TotalBlc + y
    data = {"allpayment" : allpayment, "TotalAmount": TotalAmount, "TotalBlc" : TotalBlc}
    return render(request, "payments_made.html", data)

def UserAbout(request):
    data = {} 
    return render(request, "about_us.html", data)

def UserContact(request):
    user = request.user
    if user.is_authenticated:
        initdata = {"Names" : request.user, "Email" : request.user.email}
        if request.method == "POST":
            form = UserfeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "feedback_confirm.html")
        form =  UserfeedbackForm(initial=initdata)
        data = {"forms" : form}
        return render(request, "contact_us.html", data)
    else:
        if request.method == "POST":
            form = UserfeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "feedback_confirm.html")
        form =  UserfeedbackForm()
        data = {"forms" : form}
        return render(request, "contact_us.html", data)