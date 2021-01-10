from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='user-login'),
    path('register/',views.register_view,name='user-register'),
    path('profile/',views.profile_view,name='user-profile'),
    path('logout/',views.logout_view,name='user-logout'),
]