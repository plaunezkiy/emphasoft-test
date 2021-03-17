from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from .forms import SignUpForm, ProfileForm
from .models import CustomUser


@login_required(login_url='login')
def index(request):
    profiles = CustomUser.objects.all()
    return render(request, 'index.html', context={'profiles': profiles})


@login_required(login_url='login')
def profile_redirect(request):
    return redirect('edit_profile', request.user)


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('profile-redirect')
    template_name = 'registration/signup.html'


class ProfileView(View):
    def get(self, request, username):
        profile = get_object_or_404(CustomUser, username=username)
        return render(request, 'profile.html', context={'profile': profile})


class EditProfileView(View):
    def get(self, request, username):
        profile = get_object_or_404(CustomUser, username=username)
        if request.user != profile:
            return redirect('profile', profile)
        form = ProfileForm(instance=profile)
        return render(request, 'profile.html',
                      context={'profile': profile, 'form': form})

    def post(self, request, username):
        profile = get_object_or_404(CustomUser, username=username)
        if request.user != profile:
            return redirect('profile', profile)
        form = ProfileForm(request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('profile', profile)
        return render(request, 'profile.html',
                      context={'profile': profile, 'form': form})
