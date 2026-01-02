from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import time

class ServicePackage(models.Model):
    # This is just a reference for Foreign Keys, imported from services app usually
    # But since we can't import comfortably with circular deps if we aren't careful, 
    # we will use string reference 'services.ServicePackage'
    pass

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', _('Pending')),
        ('CONFIRMED', _('Confirmed')),
        ('COMPLETED', _('Completed')),
        ('CANCELLED', _('Cancelled')),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    package = models.ForeignKey('services.ServicePackage', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.PositiveIntegerField(help_text=_("Duration in minutes"), editable=False) # Copied from package for history
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk: # New appointment
            self.duration = self.package.duration
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer} - {self.date} {self.time} ({self.status})"

class BookingSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    appointment = models.OneToOneField(Appointment, on_delete=models.SET_NULL, null=True, blank=True, related_name='booking_slot')

    class Meta:
        # Prevent creating multiple slots for same time
        unique_together = ('date', 'start_time')
        ordering = ['date', 'start_time']

    def clean(self):
        # Business Rule: Salon hours 10 AM - 8 PM
        OPENING_TIME = time(10, 0)
        CLOSING_TIME = time(20, 0)

        if self.start_time < OPENING_TIME or self.end_time > CLOSING_TIME:
            raise ValidationError(_("Appointments can only be booked between 10 AM and 8 PM."))
        
        if self.start_time >= self.end_time:
             raise ValidationError(_("End time must be after start time."))

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"{self.date} | {self.start_time} - {self.end_time} | {status}"
