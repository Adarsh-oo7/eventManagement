from django.db import models

# Create your models here.
class Events(models.Model):
    imgs=models.ImageField( upload_to='pic')
    name=models.CharField( max_length=50)
    desc=models.CharField(max_length=150)