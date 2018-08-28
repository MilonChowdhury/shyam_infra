from django.urls import path
from partners import  views



urlpatterns=[
    path('list_joint_venture_details/<project_id>/',views.JointVentureList.as_view())

]