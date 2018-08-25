from django.db import models
from project.models import ProjectDetails
# Create your models here.
class BidingCompanies(models.Model):
    project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE, blank=True, null=True)
    biding_position=models.CharField(max_length=255,blank=True,null=True)
    company_name=models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)