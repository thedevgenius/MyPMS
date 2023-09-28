from django.urls import path
from. import views

urlpatterns = [
    path('', views.TaskDispaly, name='task'),
    path('<str:id>/', views.TaskDetails, name='taskdetails'),
    path('changeassign/<str:id>/', views.ChangeAssign, name='changeassign'),
    path('addcomment/<str:id>/', views.AddComment, name='addcomment'),
]