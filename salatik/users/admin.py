from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role, CustomerAddress


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'phone', 'active')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'date_joined', 'get_role', 'active')
    list_filter = ('role__name', 'active')
    search_fields = ('username', 'email', 'phone')

    def get_role(self, obj):
        if obj.role.exists():
            return ', '.join(role.name for role in obj.role.all())
        return None
    get_role.short_description = 'Роль'

    def save_model(self, request, obj, form, change):
        # Проверяем, является ли созданный пользователь новым
        if not change:
            # Проверяем, если роль пользователя не "покупатель"
            if obj.role.upper() != "ПОКУПАТЕЛЬ":
                # Отправляем уведомление админу
                self.message_user(request, "Новый пользователь зарегистрирован. Требуется одобрение.")
        super().save_model(request, obj, form, change)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('users', 'city', 'street', 'house', 'flat')


# Регистрация моделей в административной панели
admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(CustomerAddress)
