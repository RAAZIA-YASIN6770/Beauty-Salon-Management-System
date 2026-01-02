from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom User model for Beauty Salon Management System.
    Includes support for Pakistani phone number format.
    """
    phone_regex = RegexValidator(
        regex=r'^\+92-\d{3}-\d{7}$',
        message=_("Phone number must be entered in the format: '+92-XXX-XXXXXXX'.")
    )
    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=15, 
        unique=True,
        help_text=_("Required. Format: +92-XXX-XXXXXXX")
    )
    
    # Add any additional fields if required by SRS later, otherwise AbstractUser covers most.
    
    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"
