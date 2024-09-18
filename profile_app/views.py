

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileUpdateForm

@login_required
def view_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'userprofile/view_profile.html', {'profile': profile})

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'userprofile/update_profile.html'
    success_url = '/profile/'  # Redirect to a suitable URL after successful update

    def get_object(self, queryset=None):
        # Ensure we are editing the current user's profile
        return get_object_or_404(Profile, user=self.request.user)

    def form_valid(self, form):
        profile = form.save(commit=False)
        last_donation_date = profile.last_donation_date
        availability = form.cleaned_data['availability']

        if availability and last_donation_date:
            days_since_last_donation = (timezone.now().date() - last_donation_date).days
            if days_since_last_donation < 56:
                form.add_error('availability', f'You must wait {56 - days_since_last_donation} more days before you can set your availability to true.')
                return self.form_invalid(form)

        return super().form_valid(form)

