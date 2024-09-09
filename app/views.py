from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from.forms import signupForm
from.models import *
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def signup(request):
    if request.method=='POST':
        signupform=signupForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            
            return redirect('signin')
    else:
        signupform=signupForm()
    return render(request, 'app/register.html',{"form":signupform})

def signin(request):
    if request.method=='POST':
        signinform=AuthenticationForm(data=request.POST)
        if signinform.is_valid():
            
            login(request, signinform.get_user())
            return redirect('home')
        
    else:
        signinform=AuthenticationForm()
    return render(request, 'app/login.html',{"form":signinform})

def signout(request):
    logout(request)
    return redirect('home')

def room(request):
    rooms=Rooms.objects.all()
    return render(request,'app/rooms.html',{'rooms':rooms})

def roomview(request,slug):
    room=Rooms.objects.get(slug=slug)
    messages= Messages.objects.filter(room=room)
    return render(request,'app/roomview.html',{'room':room,'messages':messages})