"""mockserver URL Configuration

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
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('register', views.register, name='register'),
    path('hello', views.hello, name='hello'),
    path('api/1/wlan/confirm_req', views.provisioning_second_step, name='provisioning_second_step'),
    path('api/1/wlan/profile_add', views.connect, name='connect'),
    path('param_cfg_result.txt', views.verify_provisioning, name='verify_provisioning'),
    path('check', views.check, name='check'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('param_device_name.txt', views.set_name, name='name_set'),
    path('api/1/netapp/set_urn', views.get_name, name='name_get'),
]
