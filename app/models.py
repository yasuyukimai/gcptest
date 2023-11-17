from django.db import models

# Create your models here.
class Model(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    
    def __str__(self):
        return self.title