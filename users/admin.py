from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        'id', 'email', 'username', 'first_name', 'last_name',
        'role', 'is_verified', 'is_active'
    )
    list_filter = (
        'role', 'is_verified', 'is_staff', 'is_superuser'
    )
    search_fields = (
        'email', 'username', 'first_name', 'last_name'
    )
    ordering = ('-created_at',)

    readonly_fields = ('last_login', 'created_at', 'updated_at')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {
            'fields': (
                'username', 'first_name', 'last_name', 'phone'
            )
        }),
        ('Permissions', {
            'fields': (
                'role', 'is_verified', 'is_active', 'is_staff', 'is_superuser', 
                'groups', 'user_permissions'
            )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'created_at', 'updated_at')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name', 'phone', 'role',
                'password1', 'password2'
            ),
        }),
    )
