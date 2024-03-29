from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Model"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                'fields': (
                    'avator',
                    'gender',
                    'bio',
                    'birthday',
                    'language',
                    'currency',
                    'superhost',
                )
            }
        ),
    )

    list_filter = (
        UserAdmin.list_filter + ('superhost',)
    )

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser',
    )
