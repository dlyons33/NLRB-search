from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='user-login'),
    path('register/',views.register,name='user-register'),
    path('profile/',views.profile,name='user-profile'),
]