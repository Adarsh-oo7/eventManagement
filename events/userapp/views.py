from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def reg(request):
    if request.POST:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'this user name is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this email is already taken')
                return redirect('register')
            else:
                user_reg=User.objects.create_user(username=username,password=password,email=email)
                user_reg.save()
                messages.info(request,'Registed Successfully')
                return redirect('/')
        else :
            messages.info(request,'Plese check Your password')
            return redirect('register')



    return render(request,'reg.html')

def login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'login Success')
            return redirect('/')
        else:
            messages.info(request,'check the username and password')
            return redirect('login')
    return render(request,'log.html')