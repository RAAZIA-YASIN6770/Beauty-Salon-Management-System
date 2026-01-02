from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Appointment, BookingSlot
from .forms import AppointmentForm
from services.models import ServicePackage
from datetime import datetime, timedelta
from django.db.models import Q, Sum
from django.utils.translation import gettext_lazy as _

class BookingView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/booking_form.html'
    success_url = reverse_lazy('appointments:dashboard')

    def get_initial(self):
        initial = super().get_initial()
        # Check URL Path parameter first (e.g. /book/1/)
        package_id = self.kwargs.get('service_id')
        
        # Fallback to Query Parameter (e.g. ?package=1)
        if not package_id:
            package_id = self.request.GET.get('package')
            
        if package_id:
            try:
                package = ServicePackage.objects.get(pk=package_id)
                initial['package'] = package
            except ServicePackage.DoesNotExist:
                pass
        return initial

    def form_valid(self, form):
        form.instance.customer = self.request.user
        response = super().form_valid(form)
        
        # Create corresponding BookingSlot
        # Calculate End Time based on package duration
        start_time = form.cleaned_data['time']
        duration = form.instance.package.duration
        
        # Simple duration addition (logic might need refinement for creating datetime then extracting time 
        # to handle day overflow, but assuming same-day appointments for Phase 1)
        # Using a dummy date to add time
        dummy_date = datetime(2000, 1, 1, start_time.hour, start_time.minute)
        end_time = (dummy_date + timedelta(minutes=duration)).time()
        
        BookingSlot.objects.create(
            date=form.cleaned_data['date'],
            start_time=start_time,
            end_time=end_time,
            is_available=False,
            appointment=self.object
        )
        
        messages.success(self.request, "Appointment booked successfully! We look forward to seeing you.")
        return response

class CustomerDashboardView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/dashboard.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(customer=self.request.user).order_by('-created_at')

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Admin dashboard for managing all appointments"""
    model = Appointment
    template_name = 'appointments/admin_dashboard.html'
    context_object_name = 'appointments'
    paginate_by = 20
    
    def test_func(self):
        """Only allow superusers/staff to access"""
        return self.request.user.is_staff or self.request.user.is_superuser
    
    def get_queryset(self):
        queryset = Appointment.objects.select_related('customer', 'package').order_by('-created_at')
        
        # Search functionality
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(
                Q(customer__username__icontains=search_query) |
                Q(customer__phone_number__icontains=search_query) |
                Q(customer__email__icontains=search_query)
            )
        
        # Status filter
        status_filter = self.request.GET.get('status', '')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate total revenue from completed appointments
        total_revenue = Appointment.objects.filter(
            status='COMPLETED'
        ).aggregate(total=Sum('package__price'))['total'] or 0
        
        context['total_revenue'] = total_revenue
        context['search_query'] = self.request.GET.get('q', '')
        context['status_filter'] = self.request.GET.get('status', '')
        
        # Count by status
        context['pending_count'] = Appointment.objects.filter(status='PENDING').count()
        context['confirmed_count'] = Appointment.objects.filter(status='CONFIRMED').count()
        context['completed_count'] = Appointment.objects.filter(status='COMPLETED').count()
        context['cancelled_count'] = Appointment.objects.filter(status='CANCELLED').count()
        
        return context

def approve_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    # Ideally should check for staff permission, but keeping it simple as requested
    appointment.status = 'CONFIRMED'
    appointment.save()
    messages.success(request, _("Appointment confirmed successfully."))
    return redirect('appointments:admin_dashboard')

def cancel_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'CANCELLED'
    appointment.save()
    
    # Also free up the slot
    if hasattr(appointment, 'booking_slot'):
        slot = appointment.booking_slot
        slot.is_available = True
        slot.save()
        
    messages.success(request, _("Appointment cancelled."))
    return redirect('appointments:admin_dashboard')

def complete_appointment(request, pk):
    """Mark appointment as completed"""
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'COMPLETED'
    appointment.save()
    messages.success(request, _("Appointment marked as completed."))
    return redirect('appointments:admin_dashboard')

