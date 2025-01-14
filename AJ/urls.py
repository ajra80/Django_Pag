"""PagAJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

    Importante incluir el app_name
"""
from django.urls import path

from . import views
from django.views.generic import TemplateView

app_name = 'AJ'
urlpatterns = [
    path('',TemplateView.as_view(template_name="AJ/home.html"),name="homeAj"),
    path('about/',views.about,name='about'),
    path('resume/',views.resume,name='resume'),
    path('services/',views.services,name='services'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('logIn/',views.LogIn,name='LogIn'),

]
