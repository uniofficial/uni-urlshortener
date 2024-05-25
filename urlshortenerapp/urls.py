from django.urls import path
from .views import create_short_link, redirect_short_link

urlpatterns = [
    path('short-links/', create_short_link, name='create_short_link'),
    path('short-links/<str:hash_value>/', redirect_short_link, name='redirect_short_link'),
]
