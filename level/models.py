from django.db import models

class Level(models.Model):
    level_name=models.CharField(max_length=255)
    parent_level = models.ForeignKey('self',on_delete= models.CASCADE,blank=True, null=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


