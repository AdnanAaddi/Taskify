from django.db import models
from users.models import ProjectUser
User=ProjectUser

class Project(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(max_length=500, default='This is Project Description')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    collaborators = models.ManyToManyField(User, related_name='collaborated_projects')

    def __str__(self):
        return self.name
    
