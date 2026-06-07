from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    # Admin paneldagi ustunlar ro'yxati
    list_display = ['first_name', 'last_name', 'email', 'is_staff', 'is_active', 'ip']
    # Tartiblash (email bo'yicha)
    ordering = ['first_name']

    # Username maydoni o'chgani uchun admin paneldagi ko'rinish guruhlarini tozalaymiz
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        ('Huquqlar', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )


admin.site.register(User, CustomUserAdmin)