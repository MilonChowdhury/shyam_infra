from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include
from .views import CustomAuthToken
from rest_framework.authtoken import views as rest_framework_views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', CustomAuthToken.as_view()),

]



