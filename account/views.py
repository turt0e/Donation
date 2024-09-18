
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from profile_app.models import Profile
from django.contrib.auth import authenticate, login


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            try:
                profile = Profile.objects.get(user=user)  # Check if the user has a profile
                login(request, user)
                return redirect('home')  # Redirect to homepage
            except Profile.DoesNotExist:
                return redirect('profile_create')  # Redirect to profile creation if profile is missing
        else:
            error = "Invalid login credentials"
    return render(request, 'login.html', {'error': error})
