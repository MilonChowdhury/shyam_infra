from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from project.models import *
from rest_framework.exceptions import APIException
from partners.models import *


class ProjectDetailsSerializer(ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=ProjectDetails
        fields='__all__'

class AddProjectVentureSerializer(ModelSerializer):
    patners = serializers.ListField(required=False)
    class Meta:
        model=ProjectDetails
        fields=['id','venture','patners']

    def update(self, instance, validated_data):
        try:
            patners = validated_data.pop('patners')
            instance.venture = validated_data.get('venture', instance.venture)
            project_id = instance.id
            instance.save()
            if validated_data.get('venture') and patners:
                for jv in patners:
                    partner_percentage = jv.pop('partner_percentage')
                    partner_details = PartnerDetails.objects.get_or_create(**jv)
                    print('partner_details:', partner_details)
                    JointVenture.objects.get_or_create(partner = partner_details[0],
                                                project_id = project_id,
                                                partner_percentage=partner_percentage)
            return instance
        except Exception as error:
            raise APIException({
                'msg': error,
                'success': 0
            })