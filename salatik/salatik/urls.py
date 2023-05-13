from django.urls import path
from core.views import ingredient_list

urlpatterns = [
    path('/', ingredient_list, name='ingredient_list'),
    # Другие пути...
]
