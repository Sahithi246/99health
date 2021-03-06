
from django.db import models
from django.utils import timezone

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    completed = models.BooleanField(blank=False)

    def __str__(self):
        return self.title