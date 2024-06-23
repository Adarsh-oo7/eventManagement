from django.contrib import admin
from .models import Events,roomBooking,Rooms
from .models import booking
# Register your models here.
admin.site.register(Events)
admin.site.register(booking)


admin.site.register(Rooms)
admin.site.register(roomBooking)