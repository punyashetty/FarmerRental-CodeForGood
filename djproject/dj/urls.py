"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from dj import views

urlpatterns = [
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.indexPage.as_view()),
    url(r'^centrehead.html',views.CenterHead.as_view()),
    url(r'^index.html',views.indexPage.as_view()),
    url(r'^statehead.html',views.StatePage.as_view()),
    url(r'^projecthead.html',views.ProjectPage.as_view()),
    url(r'^center_login.*',views.Authentication.as_view()),
    url(r'^state_login.*',views.Authentication2.as_view()),
    url(r'^my_heatmap',views.Myheat.as_view()),
    url(r'^project_login',views.Authentication3.as_view()),





]
