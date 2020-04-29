from django.db import models

# Create your models here.
class MyProjects(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    project_name = models.CharField(max_length=30)
    project_link = models.URLField(max_length=1000, db_index=True, unique=True, blank=True)
    project_desc = models.CharField(max_length=1000)
    
    def __char__(self):
        ret = self.project_name
    
    class Meta:
        unique_together = ['project_name']