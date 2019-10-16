from search import views
from django.urls import path
from .views import search_callback

urlpatterns = [
    path('', views.home, name='home'),
    path('search_callback', views.search_callback, name='search_callback'),

]
