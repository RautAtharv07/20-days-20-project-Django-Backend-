from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import registration_form,loginform

# Create your views here.


@login_required
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method=='POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user= authenticate(request,username=username,password=password) 
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = loginform()
    return render(request,'login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            login(request,username,password)
            return redirect('home')
    else:
        form = registration_form()
    return render(request,'register.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')
