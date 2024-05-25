from django.contrib import admin
from django.urls import path
from urlshortenerapp.views import create_short_link, redirect_short_link, delete_short_link, list_short_links, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('short-links/', create_short_link, name='create_short_link'),
    path('short-links/<str:hash_value>/', redirect_short_link, name='redirect_short_link'),
    path('short-links/<str:hash_value>/delete/', delete_short_link, name='delete_short_link'),
    path('short-links/all/', list_short_links, name='list_short_links'),
    path('', home, name='home'),
]
