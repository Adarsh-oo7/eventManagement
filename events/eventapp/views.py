from django.shortcuts import render,redirect
from .models import Events
from .form import bookingForms,roomBookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def events(request):
    dict_eve={
        'eve':Events.objects.all()
    }
    return render(request,'events.html',dict_eve)
 
def booking(request):
    if request.POST:
        form=bookingForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=bookingForms()
        dict_form={ 'form':form}
    return render(request,'booking.html',dict_form)


def roombooking(request):
    if request.POST:
        form=roomBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=roomBookingForm()
        dic={'form':form}
    return render (request,'roombooking.html',dic)

def contact(request):
    return render(request,'contact.html')