from rest_framework import  routers
from django.urls import path
from django.conf.urls import url,include
from project import  views


urlpatterns=[
    path('create_project/',views.ProjectCreate.as_view()),
    path('create_project/<pk>/',views.GetProjectDetailsById.as_view()),
    path('add_venture/<pk>/',views.ProjectVentureCreateView.as_view())

]