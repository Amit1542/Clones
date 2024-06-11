from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from static import *
from .models import *
from .admin import *


# Create your views here.
def index(request):
    products=productDetail.objects.all()
    status=False
    return render(request,'index.html',{'products': products,'status':status })

def show(request):
    products=productDetail.objects.all()
    return render(request,'show.html',{'products':products})

def signup_view(request):
    if request.method=="POST":
        form=signup(request.POST)
        if form.is_valid():
            try:
                return render("/")
            except:
                pass
    else:
        form=signup()
    return render(request,"sign.html")

def saveSignup(request):
    if request.method=='POST':
        full_name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        en=signup(name=full_name,email=email,password=password)
        en.save()   
        return HttpResponseRedirect("./login")



def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
 
        all_users = signup.objects.all()

        user_found = False

        for user in all_users:
            if username_or_email == user.name or username_or_email == user.email:
                user_found = True
                if password == user.password :
                    status=True
                    products=productDetail.objects.all()
                    return render(request,'index.html',{'products': products,'status':status})
                else:
                    return HttpResponse('Incorrect password!')

        if user_found==False:
            return HttpResponse("User doesn't exist" )

    return render(request, 'login.html')


def relate_view(request):
    products=productDetail.objects.all()
    return render(request,'relate.html',{'products': products})


def cart_view(request):
    if request.method=="POST":
        form=cartDetail(request.POST)
        if form.is_valid():
            try:
                return render("/")
            except:
                pass
    else:
        form=cartDetail()
    products=productDetail.objects.all()
    return render(request,"cart.html",{'products': products})

def savecart_view(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phn']
        address=request.POST['address']
        en=cartDetail(name=name,email=email,phn=phone,address=address)
        en.save()   
        return HttpResponseRedirect("./")