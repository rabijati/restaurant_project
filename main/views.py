from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import logging

logger=logging.getLogger('django')

# Create your views here.
def index(request):
    cate=None
    momo=None
    
    try:
        cate=Category.objects.all()
        pppppp
        cateid=request.GET.get('category')
        if cateid:
            momo=Momo.objects.filter(Category=cateid)
        else:
            momo=Momo.objects.all()
        
        if request.method =='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')

            Contact.objects.create(name=name,email=email,message=message,phone=phone)
            return redirect('index')
    
    except Exception as e:
        logger.error(e,exc_info=True)     

    context={
        "cate":cate,
        "momo":momo,

    }
    return render(request,'main/index.html',context)
@login_required(login_url='log_in')
def about(request):
    return render(request,'main/about.html')
def services(request):
    return render(request,'main/services.html')

@login_required(login_url='log_in')
def menu(request):
    return render(request,'main/menu.html')
def contact(request):
    return render(request,'main/contact.html')

'''
=======================================================================
=======================================================================

                           Authentication
=======================================================================
=======================================================================
'''

def register(request):
    if request.method== 'POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already exists!!")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request,"email already exists!!")
                return redirect('register')
            
            if not re.search(r"[A-Z]",password):
                messages.error(request,'your password should contain atleast one upper case')
                return redirect('register')
            
            if not re.search(r"\d",password):
                messages.error(request,'your password should contain atleast one digit')
                return redirect('register')
            
            if not re.search(r"\W",password):
                messages.error(request,'your password should contain atleast specific character')
                return redirect('register')

            try:
                validate_password(password)
                User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password)
                return redirect('log_in')
            except ValidationError as e:
                for i in e.messages:
                    messages.error(request,i)
                return redirect('register')
        else:
            messages.error(request,"Your password and confirm password doesn't match!!")
            return redirect('register')

    return render(request,'auth/register.html')


def log_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        remember_me=request.POST.get('remember_me')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'username is not register yet')
            return redirect('log_in')
        

        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if remember_me:
                request.session.set_expiry(60)
            else:
                request.session.set_expiry(0)
            next=request.POST.get('next','')

            return redirect(next if next else 'index')
        else:
            messages.error(request,"password doesnot match!!")
            return redirect('log_in')
    
    next=request.GET.get('next','')
    return render(request,'auth/login.html',{'next':next})

def log_out(request):
    logout(request)
    return redirect('log_in')


def split(request):
    total=0
    if request.method=='POST':
        counts=request.POST.get('count')
        counts1=counts.split()
        total=len(counts1)
    return render(request,'split/split.html',{'total':total})

@login_required(login_url='log_in')
def change_password(request):
    form=PasswordChangeForm(data=request.POST, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('log_in')
    
    return render(request,'auth/change_password.html', {'abc':form})

