from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        """ Override clean method for custom validation.
        """

        cleaned_data = self.cleaned_data
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if (email and password):
            if User.objects.filter(email=email).exists():
                user = authenticate(email=email, password=password)
                if not user:
                    self._errors['password'] = self.error_class([
                            "Password you entered is incorrect."])
                    raise forms.ValidationError("")
                elif not user.is_active:
                    self._errors['email'] = self.error_class([
                        "Your account is not active."])
                    raise forms.ValidationError("")

            else:
                self._errors['email'] = self.error_class([
                        "This email is not registered."])
                raise forms.ValidationError("")

        return cleaned_data