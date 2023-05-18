from rest_framework import viewsets

from api.serializers import (
    ComponentSerializer,
    DeliverySerializer,
    OrderSerializer,
    SaladSerializer,
    PaymentSerializer
)
from core.models import Component, Delivery, Order, Salad, Payment


class ComponentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для взаимодейтсвия с компонентами салатов.
    """
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class SaladViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для взаимодействия с салатами.
    """
    queryset = Salad.objects.all()
    serializer_class = SaladSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для взаимодейтсвия с отзывами.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для доставки.
    """
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для оплаты.
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
