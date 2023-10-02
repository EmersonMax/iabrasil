from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import CustomUser  # Importe o modelo de usuário

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        help_text="Informe um email válido."
    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(
        max_length=30,
        required=False,
        help_text=""
    )

    class Meta:
        model = CustomUser  # Use o modelo de usuário personalizado
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")