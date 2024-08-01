from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#from .models import User
from .forms import UserCreationForm, UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    #To add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['id', 'username',  'firstName', 'lastName', 'role']
    list_filter = ['username']
    
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('firstName', 'lastName')}),
        ('Permissions', {'fields': ('is_staff', 'role')}),
    ]

    add_fieldsets = [
        (None, {
            'classes':('wide',),
            'fields': ('username', 'firstName', 'lastName', 'password', 'password_2', 'gender', 'role')
        }),
    ]

    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = []


admin.site.register(User, UserAdmin)
# remove the Group model from the admin, not needed.
#admin.site.unregister(Group)
