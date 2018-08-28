from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from project.serializers import *
from django.contrib.auth.models import User
from project.models import *

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class ProjectCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset =ProjectDetails.objects.all()
    serializer_class = ProjectDetailsSerializer

class GetProjectDetailsById(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = ProjectDetails.objects.all()
    serializer_class =ProjectDetailsSerializer

class ProjectVentureCreateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = ProjectDetails.objects.all()
    serializer_class = AddProjectVentureSerializer