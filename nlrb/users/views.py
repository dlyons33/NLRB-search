from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from .models import WeekSummary

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
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "form":form,
        "btn_label":"Submit",
        "title":"Register",
    }
    return render(request,"pages/auth.html",context=context,status=200)

def profile_view(request):
    return HttpResponse("This is the user's PROFILE page :)")

# WILL WANT TO MOVE HOME_VIEW TO "CASES" APP
def home_view(request):
    summary = WeekSummary.objects.order_by('-id').first()
    context = {
        'summary':summary.summary_string,
    }
    return render(request,"pages/home.html",context=context,status=200)

def about_view(request):
    return render(request,"pages/about.html",context={},status=200)