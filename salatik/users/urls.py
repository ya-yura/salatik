from django.urls import path
from .views import register, edit_profile, profile

urlpatterns = [
    # Other URL patterns
    path('new/', register, name='register'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
]
