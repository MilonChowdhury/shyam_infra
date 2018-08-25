from django.db import models
from level.models import  Level
from document_type.models import DocumentType
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.category_name)

class ProjectDetails(models.Model):
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Working_on'),
        (2, 'Complete'),
        (3, 'Reject'),
    )
    VENTURE_CHOICES = (
        (0, 'Individual'),
        (1, 'Joint_venture')
    )
    project_name=models.CharField(max_length=255,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_approved=models.BooleanField(default=False)
    status=models.IntegerField(choices=STATUS_CHOICES, default=0,blank=True,null=True)
    current_level=models.ForeignKey(Level,on_delete=models.CASCADE,blank=True,null=True)
    venture=models.IntegerField( choices=VENTURE_CHOICES, default=0,blank=True,null=True)

    def __str__(self):
        return str(self.id)


class ProjectLevel(models.Model):
    project=models.ForeignKey(ProjectDetails,on_delete=models.CASCADE,blank=True,null=True)
    level=models.ForeignKey(Level,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.BooleanField(default=True)
    reason=models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ProjectDocument(models.Model):
    project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE, blank=True, null=True)
    document_type=models.ForeignKey(DocumentType,on_delete=models.CASCADE, blank=True, null=True)
    document_description=models.TextField(blank=True, null=True)
    document_file=models.FileField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ProjectQuotations(models.Model):
    project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE, blank=True, null=True)
    price=models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ProjectApprovedDetails(models.Model):
    project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE, blank=True, null=True)
    biding_position=models.CharField(max_length=255,blank=True,null=True)
    loi_issued=models.BooleanField(default=False)
    loi_file=models.FileField(blank=False, null=False)
    reason=models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
