from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WeekSummary
from .forms import UserRegistrationForm

def login_view(request):
    form = AuthenticationForm(request,data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        return redirect("home-page")
    context = {
        "form":form,
        "btn_label":"Login",
        "title":"Login",
    }
    return render(request,"pages/auth.html",context=context,status=200)

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home-page")
    context = {
        "form":None,
        "btn_label":"Logout",
        "title":"Are you sure you want to logout?",
    }
    return render(request,"pages/auth.html",context=context,status=200)

def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        messages.success(request,f'Account created for {username}!')
        user = form.save(commit=True)
        login(request,user)
        return redirect("home-page")
    context = {
        "form":form,
        "btn_label":"Submit",
        "title":"Register",
    }
    return render(request,"pages/auth.html",context=context,status=200)

@login_required
def profile_view(request):
    return render(request,"pages/profile.html",context={},status=200)

# WILL WANT TO MOVE HOME_VIEW TO "CASES" APP
def home_view(request):
    summary = WeekSummary.objects.order_by('-id').first()
    if request.user.is_authenticated:
        context = {
            'summary':summary.summary_string,
        }
        return render(request,"pages/user_home.html",context=context,status=200)
    else:
        context = {
            'summary':summary.summary_string,
        }
        return render(request,"pages/home.html",context=context,status=200)

def about_view(request):
    return render(request,"pages/about.html",context={},status=200)