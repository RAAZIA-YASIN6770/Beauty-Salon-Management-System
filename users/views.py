from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, UserProfileForm
from appointments.models import Appointment
from services.models import ServicePackage
from django.utils import timezone
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('service_list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) # Auto-login after registration
        return redirect(self.success_url)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('appointments:dashboard')

class CustomerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Upcoming Appointments
        context['upcoming_appointments'] = Appointment.objects.filter(
            customer=user,
            date__gte=timezone.now().date()
        ).order_by('date', 'time')
        
        # Appointment History (Past)
        context['appointment_history'] = Appointment.objects.filter(
            customer=user,
            date__lt=timezone.now().date()
        ).order_by('-date', '-time')
        
        # Recommended Packages (Simple logic: Random or latest 3)
        context['recommended_packages'] = ServicePackage.objects.filter(is_active=True).order_by('?')[:3]
        
        return context

class ProfileView(LoginRequiredMixin, UpdateView):
    """View for editing user profile"""
    model = None  # Will be set dynamically
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, _("Profile updated successfully!"))
        return super().form_valid(form)

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """View for changing user password"""
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, _("Password changed successfully!"))
        return super().form_valid(form)

