from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse



def home(request):
    return render(request,'home.html')


def register(request):

    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                 messages.info(request,'Username Taken')
                 return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, 'Email Taken')
                 return redirect('register')
            else:
                 user= User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                 user.save();
                 print("user created")
                 return redirect('login/')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')
    else:
         return render(request,'register.html')


def registerrr(request):

    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                 messages.info(request,'Username Taken')
                 return redirect('registerrr')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, 'Email Taken')
                 return redirect('registerrr')
            else:
                 user= User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                 user.save();
                 print("user created")
                 return redirect('loginnn')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('registerrr')
    else:
         return render(request,'registerrr.html')


def registerr(request):

    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                 messages.info(request,'Username Taken')
                 return redirect('registerr')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, 'Email Taken')
                 return redirect('registerr')
            else:
                 user= User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                 user.save();
                 print("user created")
                 return redirect('loginn')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('registerr')
    else:
         return render(request,'registerr.html')




def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('out/deatils')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def loginn(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'submitted.html')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request, 'submitted.html')
    else:
      return render(request,'loginn.html')

def loginnn(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('submitt')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('submitt')
    else:
      return render(request,'loginnn.html')



def aboutt(request):
    return render(request,'aboutt.html')


def submitt(request):
    if request.method == 'POST':
       return render(request,'submitt.html')
    else:
      return redirect('done')


def done(request):
    return render(request,'done.html')
