from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompExamChoice, name='CompExamChoice'),
    path('preview/', views.preview, name='preview'),
    path('success/', views.success, name='success'),
]
