from django.contrib import admin
from django.urls import path
from core.views import ingredient_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ingredient_list, name='ingredient_list'),
    # Другие пути...
]
