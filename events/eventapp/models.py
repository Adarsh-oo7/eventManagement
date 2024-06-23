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


class Rooms(models.Model):
    img=models.ImageField(upload_to='pic')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20)
    availability = models.BooleanField(default=True)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=250)
    def __str__(self):
        return self.room_number

class roomBooking(models.Model):
    cus_name=models.CharField(max_length=20)
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    cus_phone=models.CharField(max_length=12)
    booking_date=models.DateField()
    vacate_date=models.DateField()
    booking_on=models.DateField(auto_now=True)
