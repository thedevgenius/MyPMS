from django.urls import path
from. import views

urlpatterns = [
    path('', views.Blog, name='blog'),
    path('<str:slug>/', views.BlogDetails, name='blogdetail'),
]