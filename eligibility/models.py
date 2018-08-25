from django.db import models
from project.models import ProjectDetails
from django.contrib.auth.models import User

class TechnicalEligibility(models.Model):
    project=models.ForeignKey(ProjectDetails,on_delete=models.CASCADE,blank=True,null=True)
    construction_work_experience=models.CharField(max_length=255,blank=True,null=True)
    key_work_experience=models.TextField(blank=True,null=True)
    similar_nature_of_work=models.TextField(blank=True,null=True)
    machinery_list=models.TextField(blank=True,null=True)
    others=models.TextField(blank=True,null=True)
    reason=models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class FinancialEligibility(models.Model):
    project=models.ForeignKey(ProjectDetails,on_delete=models.CASCADE,blank=True,null=True)
    bid_capacity=models.TextField(blank=True,null=True)
    turn_over=models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)
    key_word_value=models.CharField(max_length=255,blank=True,null=True)
    net_worth=models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)
    other=models.TextField(blank=True,null=True)
    status=models.BooleanField(default=True)
    reason=models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class InitialCosting(models.Model):
    project=models.ForeignKey(ProjectDetails,on_delete=models.CASCADE,blank=True,null=True)
    initial_cost=models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)
    status = models.BooleanField(default=True)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)