from django.urls import path

from . import  views

app_name = 'itemsdetails'

urlpatterns = [
    path('new/', views.newItem, name='new'),
    path('<int:pk>/', views.details, name = 'detail'),]