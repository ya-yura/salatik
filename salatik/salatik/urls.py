from django.contrib import admin
from django.urls import path, include
from core.views import ingredient_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # Все адреса с префиксом auth/ 
    # будут перенаправлены в модуль django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')), 
    path('', ingredient_list, name='ingredient_list'),
    path('api/', include('api.urls')),
    path('salad/', include('core.urls')),
    path('users/', include('users.urls')),
    path('kitchen/', include('kitchen.urls')),
    # Другие пути...
]
