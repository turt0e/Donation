# profile/forms.py
from django import forms
from .models import Profile
from django.core.exceptions import ValidationError
from django.utils import timezone


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'availability',
                  'last_donation_date']
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_availability(self):
        availability = self.cleaned_data.get('availability')
        last_donation_date = self.cleaned_data.get('last_donation_date')

        if availability and last_donation_date:
            # Check if the user is trying to make themselves available
            days_since_last_donation = (timezone.now().date() - last_donation_date).days
            if days_since_last_donation < 56:
                raise ValidationError(
                    f"You must wait at least {56 - days_since_last_donation} more days before you can set your availability to true.")

        return availability

    def clean(self):
        cleaned_data = super().clean()
        last_donation_date = cleaned_data.get('last_donation_date')

        if last_donation_date and last_donation_date > timezone.now().date():
            self.add_error('last_donation_date', "Last donation date cannot be in the future.")

        return cleaned_data
