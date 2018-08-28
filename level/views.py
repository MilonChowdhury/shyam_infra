from django.shortcuts import render

from level.serializers import *
from rest_framework.generics import *

class LevelDropDownListView(ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
