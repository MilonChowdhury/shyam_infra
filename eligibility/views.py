from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from eligibility.models import *
from eligibility.serializers import *

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class TechnicalEligibilityCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = TechnicalEligibility.objects.all()
    serializer_class = TechnicalEligibilitySerializer

class FinancialEligibilityCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = FinancialEligibility.objects.all()
    serializer_class = FinancialEligibilitySerializer

class InitialCostingCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = InitialCosting.objects.all()
    serializer_class = InitialCostingSerializer