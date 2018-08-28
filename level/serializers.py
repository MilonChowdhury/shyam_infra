from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer
from level.models import *


class LevelSerializer(ModelSerializer):

    class Meta:
        model=Level
        fields='__all__'