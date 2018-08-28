from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import *
from partners.serializers import *
from partners.models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class JointVentureList(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class =JointVentureSerializer
    lookup_field = 'project_id'
    def get_queryset(self):
        project_id=self.kwargs['project_id']
        queryset=JointVenture.objects.filter(project_id=project_id,is_deleted=False)
        return  queryset