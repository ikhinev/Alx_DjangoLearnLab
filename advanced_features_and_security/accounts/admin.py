from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add custom fields to the admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Explicit registration (required for your checker)
admin.site.register(CustomUser, CustomUserAdmin)
