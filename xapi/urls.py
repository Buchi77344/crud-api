from django.urls import path 
from . import views

urlpatterns = [
    path('',views.xapi),
    path('create',views.create),
    path('itemlist',views.itemlist),
    path('details/<str:pk>',views.details),
    path('update/<str:pk>',views.update),
    path('delete/<str:pk>',views.delete),
]
