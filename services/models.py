from django.db import models
from django.utils.translation import gettext_lazy as _

class ServicePackage(models.Model):
    CATEGORY_CHOICES = [
        ('BRIDAL', _('Bridal')),
        ('HAIR', _('Hair Care')),
        ('SKIN', _('Skin Care')),
        ('MAKEUP', _('Makeup')),
        ('OTHER', _('Other')),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text=_("Price in PKR"))
    duration = models.PositiveIntegerField(help_text=_("Duration in minutes"))
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_category_display()}"

    class Meta:
        verbose_name = _("Service Package")
        verbose_name_plural = _("Service Packages")
