from django.contrib import admin
from .models import Appointment, BookingSlot

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'package', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('customer__username', 'customer__email', 'notes')
    date_hierarchy = 'date'

@admin.register(BookingSlot)
class BookingSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', 'is_available', 'appointment')
    list_filter = ('date', 'is_available')
    date_hierarchy = 'date'
