from django import forms
from .models import Appointment, BookingSlot
from django.utils import timezone
from datetime import datetime, time, timedelta

class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Appointment
        fields = ['package', 'date', 'time', 'notes']
        widgets = {
             'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        selected_time = cleaned_data.get('time')

        if not date or not selected_time:
            return

        # Combine date and time for validation
        booking_datetime = datetime.combine(date, selected_time)
        now = datetime.now()
        
        # 1. Lead Time Validation (Min 2 hours)
        if booking_datetime < now + timedelta(hours=2):
            raise forms.ValidationError("Appointments must be booked at least 2 hours in advance.")

        # 2. Salon Hours Validation (10 AM - 8 PM)
        # Note: This is also checked in BookingSlot model, but good to have in form for user feedback
        OPENING_TIME = time(10, 0)
        CLOSING_TIME = time(20, 0)
        if selected_time < OPENING_TIME or selected_time > CLOSING_TIME:
             raise forms.ValidationError("Salon hours are between 10:00 AM and 8:00 PM.")

        # 3. Availability Validation (Double Booking)
        # Check if any slot exists for this date/time. 
        # Ideally, we should check duration overlap, but for Phase 1 basic slot check:
        # Assuming slots are fixed or we check start time collision.
        # A more robust check would see if (Start < ExistingEnd) and (End > ExistingStart).
        # For this form, we check if a booking slot already exists at this exact start time.
        if BookingSlot.objects.filter(date=date, start_time=selected_time, is_available=False).exists():
            raise forms.ValidationError("This time slot is already booked. Please choose another time.")

        return cleaned_data
