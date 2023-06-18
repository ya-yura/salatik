from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role, CustomerAddress


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_superuser')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('users', 'city', 'street',
                    'house', 'flat')


# Регистрация моделей в административной панели
admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(CustomerAddress)
