from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about_view(request):
    """About page view"""
    return render(request, 'core/about.html')

def contact_view(request):
    """Contact page view"""
    return render(request, 'core/contact.html')

