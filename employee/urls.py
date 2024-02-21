from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('view/', views.view, name = 'view'),
    path('create/', views.create, name = 'create'),
    path('delete/', views.delete, name = 'delete'),
    path('delete/<int:emp_id>/', views.delete, name = 'delete'),
    path('filter/', views.filter, name = 'filter'), 
]