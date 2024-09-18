# profile/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
from account.models import CustomUser, CustomUserManager

class Profile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)  # A+, B-, O, etc.
    availability = models.BooleanField(default=False)
    last_donation_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def can_donate(self):
        """Returns True if the user can change availability to True (at least 56 days after last donation)."""
        if not self.last_donation_date:
            return True
        days_since_last_donation = (timezone.now().date() - self.last_donation_date).days
        return days_since_last_donation >= 56

    def __str__(self):
        return f"{self.username.email}'s Profile"
