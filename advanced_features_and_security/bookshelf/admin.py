from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser  # Import from accounts

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add your custom fields to the admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Explicit registration required for the checker
admin.site.register(CustomUser, CustomUserAdmin)
