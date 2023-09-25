from django.urls import path
from. import views

urlpatterns = [
    path('', views.Projects, name='project'),
    # path('files/', views.Files, name='files'),
    path('add-file/<int:id>/', views.AddFiles, name='addfiles'),
    path('<str:slug>/', views.ProjectDetails, name='projectdetails'),
    path('edit/<int:id>/', views.ProjectEdit, name='projectedit'),
    
]