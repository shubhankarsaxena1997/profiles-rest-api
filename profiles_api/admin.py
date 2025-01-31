from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin
from django.contrib import admin
from .models import *

class CustomTokenAdmin(TokenAdmin):
    search_fields = ['name']  # Assuming you want to search by name

admin.site.register(Token, CustomTokenAdmin)

admin.site.register(UserProfile)
