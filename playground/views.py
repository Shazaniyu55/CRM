from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def say_hello(request):
    return render(request, 'index.html')



def nav_bar(request):
    return render(request, 'nav.html')


def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        
        my_user = User.objects.create_user(firstname, lastname, email, pass1)
        my_user.save()
        return redirect('login')
        

    return render(request, 'signup.html')

