from django.urls import path
from level import  views


urlpatterns=[
    path('level_dropdown/',views.LevelDropDownListView.as_view()),

]