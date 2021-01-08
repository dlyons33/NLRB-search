from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import WeekSummary

def login(request):
    return HttpResponse("This is the LOGIN page :)")

def register(request):
    return HttpResponse("This is the REGISTRATION page :)")

def profile(request):
    return HttpResponse("This is the user's PROFILE page :)")

# WILL WANT TO MOVE HOME_VIEW TO "CASES" APP
def home_view(request):
    summary = WeekSummary.objects.order_by('-id').first()
    context = {
        'summary':summary.summary_string,
    }
    return render(request,"pages/home.html",context=context,status=200)