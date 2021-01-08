from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,HistoricalSearches,SavedCases

admin.site.register(User,UserAdmin)
admin.site.register(HistoricalSearches)
admin.site.register(SavedCases)