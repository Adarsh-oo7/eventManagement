from django.db import models

# Create your models here.
class Events(models.Model):
    imgs=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=150)
    def __str__(self):
        return self.name


class booking(models.Model):
    cus_name=models.CharField( max_length=50)
    cus_ph=models.CharField( max_length=12)
    name=models.ForeignKey(Events,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)
