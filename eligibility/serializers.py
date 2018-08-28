from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from eligibility.models import *
from rest_framework.exceptions import APIException


class TechnicalEligibilitySerializer(ModelSerializer):
    level = serializers.IntegerField(required=False)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=TechnicalEligibility
        fields=['id','project','construction_work_experience',
                'key_work_experience','similar_nature_of_work','machinery_list'
            ,'others','reason','status','level','created_by']

    def create(self, validated_data):
        try:
            level = validated_data.pop('level')
            project = validated_data.get('project')
            tech_eligible_status = validated_data.get('status')
            reason = validated_data.get('reason')
            if not tech_eligible_status and not reason:
                raise Exception("Please give the reason")
            else:
                technical_eligibility = TechnicalEligibility.objects.create(**validated_data)
                ProjectLevel.objects.get_or_create(project = project, level_id=level,status=tech_eligible_status,reason=reason)
                pro_details = ProjectDetails.objects.filter(pk=str(project))
                for project_data in pro_details:
                    if not tech_eligible_status or project_data.status==3:
                        project_data.status = 3
                    else:
                        project_data.status = 1
                    project_data.current_level_id = level
                    project_data.save()
                return technical_eligibility
        except Exception as e:
            raise APIException({"error":e,"success":0})


class FinancialEligibilitySerializer(ModelSerializer):
    level = serializers.IntegerField(required=False)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=FinancialEligibility
        fields=['id','project','bid_capacity','turn_over','key_word_value',
                'net_worth','other','status','reason','level','created_by']

    def create(self, validated_data):
        try:
            level=validated_data.pop('level')
            project=validated_data.get('project')
            status=validated_data.get('status')
            reason=validated_data.get('reason')
            if not status and not reason:
                raise Exception("Please give the reason")
            else:
                financial_eligibility=FinancialEligibility.objects.create(**validated_data)
                ProjectLevel.objects.get_or_create(project=project,level_id=level,status=status,reason=reason)
                pro_details = ProjectDetails.objects.filter(pk=str(project))
                for project_data in pro_details:
                    if not status or project_data.status==3:
                        project_data.status = 3
                    else:
                        project_data.status = 1
                    project_data.current_level_id = level
                    project_data.save()
                return  financial_eligibility
        except Exception as e:
            raise APIException({"error":e,"success":0})


class InitialCostingSerializer(ModelSerializer):
    level = serializers.IntegerField(required=False)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=InitialCosting
        fields=['id','project','initial_cost','status','reason','level','created_by']
    def create(self, validated_data):
        try:
            level = validated_data.pop('level')
            project = validated_data.get('project')
            status = validated_data.get('status')
            reason = validated_data.get('reason')
            if not status and not reason:
                raise  Exception("Please give the reason")
            else:
                initial_costing=InitialCosting.objects.create(**validated_data)
                ProjectLevel.objects.get_or_create(project=project, level_id=level,status=status,reason=reason)
                pro_details = ProjectDetails.objects.filter(pk=str(project))
                for project_data in pro_details:
                    if not status or project_data.status==3:
                        project_data.status = 3
                    else:
                        project_data.status = 1
                    project_data.current_level_id=level
                    project_data.save()
                return initial_costing
        except Exception as e:
            raise APIException({"error":e,"success":0})

