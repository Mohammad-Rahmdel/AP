"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from portal import views

app_name = 'portal'

urlpatterns = [
    url(r'^st_courses/',views.st_cources,name='st_cources'),
    url(r'^change_pw/$',views.change_pw,name='change_pw'),
    url(r'^home/$',views.home,name='home'),
    url(r'^edit_info/',views.edit_info,name='edit_info'),
    url(r'^register/',views.register,name='register'),
    url(r'^add_course/',views.add_course,name='add_course'),
    url(r'^user_login/',views.user_login,name='user_login'),
]
