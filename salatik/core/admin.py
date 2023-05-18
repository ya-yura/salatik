from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import IngredientType, Ingredient, Salad, Component, Order, Payment, Delivery


class IngredientTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available', 'created_at', 'updated_at')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'is_available', 'created_at', 'updated_at')


class SaladAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available', 'created_at', 'updated_at')


class ComponentAdmin(admin.ModelAdmin):
    list_display = ('salad', 'ingredient', 'weight', 'order',
                    'is_available', 'created_at', 'updated_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'salad', 'status', 'total_price',
                    'created_at', 'updated_at')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'timestamp')


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'courier', 'address', 'status',
                    'delivery_fee', 'created_at', 'updated_at')


# Регистрация моделей в административной панели
admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Salad, SaladAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Delivery, DeliveryAdmin)
