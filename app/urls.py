from django.urls import path
from . import views

urlpatterns = [
    path('header/create/', views.header_create_view, name='header_create'),
]