from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from partners.models import *


class PartnerDetailsSerializer(ModelSerializer):
    class Meta:
        model=PartnerDetails
        fields=['id','partner_name','contact_no','address','pin_code']



class JointVentureSerializer(ModelSerializer):
    partner_details = PartnerDetailsSerializer(many=True,read_only=True)
    class Meta:
        model=JointVenture
        fields=['id','partner_percentage','partner_details']