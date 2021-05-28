from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
]