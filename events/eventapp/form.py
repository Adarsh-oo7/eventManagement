from django import forms 
from .models import booking,roomBooking


class DateInput(forms.DateInput):
    input_type='date'

class bookingForms(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'
        widgets={
            'booking_date':DateInput(),
        }


        labels={
            'cus_name':"Customer Name:",
            'cus_ph':"Customer Phone:",
            'name':"Event Name",
            'booking_date':'Booking Date'
        }


class roomBookingForm(forms.ModelForm):

    class Meta:
        model=roomBooking
        fields='__all__'
        widgets={
            'booking_date':DateInput(),
            'vacate_date':DateInput()
        }

       

        labels={
            'cus_name':"Enter Your Name",
            'room':"select Room",
            'cus_phone':"Phone Number",
            'booking_date':'Select the date',
            'vacate_date':'Select the vacte date',
            
        }
