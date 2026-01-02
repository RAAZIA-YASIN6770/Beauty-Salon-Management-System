from django.urls import path
from . import views

urlpatterns = [
    path('', views.PackageListView.as_view(), name='service_list'),
    path('<int:pk>/', views.PackageDetailView.as_view(), name='service_detail'),
]
