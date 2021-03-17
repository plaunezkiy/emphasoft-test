from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name',
                  'birth_date', 'email', 'city', 'bio', 'avatar')
