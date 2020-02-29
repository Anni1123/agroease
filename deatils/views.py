from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def wishlist(request):
    return render(request, 'wishlist.html')



def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def blog_single(request):
    return render(request, 'blog-single.html')



def cart(request):
    return render(request, 'cart.html')


def complain(request):
    return render(request, 'complain.html')


def data(request):
    return render(request,  'data.html')


def suggest(request):
    return render(request, 'suggest.html')


def register1(request):
    return render(request, 'register1.html')


def expert(request):
    return render(request, 'expert.html')



def online(request):
    return render(request, 'onlineretails.html')


def logout(request):
    auth.logout(request)
    return redirect('/')





def product_single(request):
    return render(request, 'product_single.html')



def index(request):
    return render(request,'index.html')