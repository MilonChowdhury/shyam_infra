from django.db import models
from project.models import  ProjectDetails
# Create your models here.
class PartnerDetails(models.Model):
    partner_name=models.CharField(max_length=255,blank=True,null=True)
    contact_no=models.BigIntegerField(max_length=15,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    pin_code=models.IntegerField(max_length=6,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return  str(self.id)


class JointVenture(models.Model):
    partner=models.ForeignKey(PartnerDetails,on_delete=models.CASCADE,blank=True,null=True)
    project=models.ForeignKey(ProjectDetails,on_delete=models.CASCADE,blank=True,null=True)
    partner_percentage=models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)