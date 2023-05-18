from django.urls import include, path
from rest_framework import routers

from api.views import (
    ComponentViewSet,
    DeliveryViewSet,
    OrderViewSet,
    SaladViewSet,
    PaymentViewSet
)

router = routers.DefaultRouter()

router.register('components', ComponentViewSet, basename='components')
router.register('salads', SaladViewSet, basename='salads')
router.register('orders', OrderViewSet, basename='orders')
router.register('delivery', DeliveryViewSet, basename='delivery')
router.register('payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls))
]
