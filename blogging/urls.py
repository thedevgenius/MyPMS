"""
URL configuration for blogging project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_view
from account import views as acc_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', core_view.Home, name='home'),
    path('blog/', include('blog.urls')),
    path('project/', include('project.urls')),
    path('task/', include('task.urls')),
    path('registration/', acc_view.Registration, name='registration'),
    path('login/', acc_view.Login, name='login'),
    path('logout/', acc_view.Logout, name='logout'),
    path('profile/', acc_view.Profile, name='profile'),
    path('theme/', core_view.Theme, name='themechange'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)