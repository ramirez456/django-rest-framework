from email.mime import image
from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    technology = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
