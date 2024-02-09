from django.shortcuts import render,redirect, get_object_or_404
from .models import taskData
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm, LoginForm, data
# from django.views.decorators.cache import cache_control

# Create your views here
def login(req):
    if req.method == 'POST':
        form = LoginForm(request=req, data=req.POST)
        print('ok')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            print("ok")
            if user is not None:
                auth_login(req, user)
                messages.success(req, "Hello "+username)
                return redirect('home')
        else:
            messages.error(req, "Username or Password is invalid", extra_tags="danger")
    else:
        form = LoginForm()
        print("not ok")

    return render(req, "login.html", {'form':form})

def signup(req):
    if req.method=="POST":
        form = RegistrationForm(req.POST)
        print("ok")
        
        if form.is_valid():
            form.save()
            ("ok s")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request=req,username=username, password=password)
            
            auth_login(req, user)

            messages.error(req, "Username or Password is invalid", extra_tags="danger")

            return redirect("home")
        else:
            messages.error(req, "Something wrong", extra_tags="danger")
    else:
        form = RegistrationForm()
        print("not ok")
    return render(req, "register.html", {'form':form})

@login_required(login_url='login')
@never_cache
def home(req):
    if req.method =='POST':
        form = data(req.POST)
        print("aa")
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect('tasks')
        else:
            print("bb")
            messages.error(req, "Enter your task and description", extra_tags="danger")
            print("cc")
    else:
        form = data()
    return render(req, "home.html")

@login_required(login_url='login')
@never_cache
def task(req):
    allTasks = taskData.objects.filter(user=req.user)
    
    return render(req, "tasks.html", {"tasks": allTasks})

@login_required(login_url='login')
@never_cache
def delete(req, id):
    delTask = get_object_or_404(taskData, id = id)
    delTask.delete()
    messages.success(req, "Task deleted successfully")
    return redirect('tasks')

@login_required(login_url='login')
@never_cache
def logout(req):
    auth_logout(req)
    return redirect("login")