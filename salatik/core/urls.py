from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Маршрут для отображения формы поиска
    # path('search/', views.search_salads, name='search'),

    # Маршрут для обработки запроса поиска
    # path('search/results/', views.search_results, name='search_results'),

    path('', views.ingredient_list, name='ingredient_list'),
    path('place_order/', views.place_order, name='place_order'),
]
