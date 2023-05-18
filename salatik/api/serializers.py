from rest_framework import serializers

from core.models import Component, Delivery, Order, Salad, Payment


class ComponentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для компонентов.
    """

    class Meta:
        fields = ['salad', 'ingredient', 'weight', 'order']
        model = Component


class SaladSerializer(serializers.ModelSerializer):
    """
    Сериализатор для компонентов.
    """

    class Meta:
        fields = ['name', 'description']
        model = Salad


class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для заказов.
    """

    class Meta:
        fields = ['user', 'salad', 'status', 'total_price']
        model = Order


class DeliverySerializer(serializers.ModelSerializer):
    """
    Сериализатор для доставки.
    """

    class Meta:
        fields = ['order', 'courier', 'address', 'status', 'delivery_fee']
        model = Delivery


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для оплаты.
    """

    class Meta:
        fields = ['order', 'amount', 'timestamp']
        model = Payment
