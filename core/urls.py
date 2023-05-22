from django.urls import path
from . import views

urlpatterns = [
    path('box1/', views.box1, name='box1'),
    path('box2/', views.box2, name='box2'),
]