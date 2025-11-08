from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=255,
        validators=[EmailValidator(message="Enter a valid email address.")],
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control'
        }),
        min_length=8,
        max_length=128
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # # Optional: enforce password strength
        # if not re.search(r'[A-Z]', password):
        #     raise ValidationError("Password must contain at least one uppercase letter.")
        # if not re.search(r'[a-z]', password):
        #     raise ValidationError("Password must contain at least one lowercase letter.")
        # if not re.search(r'[0-9]', password):
        #     raise ValidationError("Password must contain at least one digit.")
        # if not re.search(r'[\W_]', password):
        #     raise ValidationError("Password must contain at least one special character.")

        return password
