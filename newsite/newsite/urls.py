"""
URL configuration for newsite project.

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
from django.urls import path,include
from polls import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views



# Added path for pages inserted
#Used URL pattenrs for all apps created.
urlpatterns = [

    path('', include("django.contrib.auth.urls")),
    path('', include("user_auth.urls")),
    path("", TemplateView.as_view(template_name="login.html"), name="home"),
    path('home/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),



]


