from django.urls import include, path
from core.views import ingredient_list

urlpatterns = [
    path('/', ingredient_list, name='ingredient_list'),
    path('api/', include('api.urls')),
]
