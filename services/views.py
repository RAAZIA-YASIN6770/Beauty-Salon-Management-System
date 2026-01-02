from django.views.generic import ListView, DetailView
from .models import ServicePackage

class PackageListView(ListView):
    model = ServicePackage
    template_name = 'services/package_list.html'
    context_object_name = 'packages'
    queryset = ServicePackage.objects.filter(is_active=True)

class PackageDetailView(DetailView):
    model = ServicePackage
    template_name = 'services/package_detail.html'
    context_object_name = 'package'
    queryset = ServicePackage.objects.filter(is_active=True)
