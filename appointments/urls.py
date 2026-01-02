from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/', views.BookingView.as_view(), name='book_appointment'),
    path('book/<int:service_id>/', views.BookingView.as_view(), name='book_appointment'),
    path('dashboard/', views.CustomerDashboardView.as_view(), name='dashboard'),
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('approve/<int:pk>/', views.approve_appointment, name='approve_appointment'),
    path('cancel/<int:pk>/', views.cancel_appointment, name='cancel_appointment'),
    path('complete/<int:pk>/', views.complete_appointment, name='complete_appointment'),
]
