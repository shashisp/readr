from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):

        cleaned_data = self.cleaned_data
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if (email and password):
            db_user_query = User.objects.filter(email=email)
            if db_user_query:
                # import ipdb; ipdb.set_trace()
                user = authenticate(email=email, password=password)
                if not db_user_query[0].is_active:
                    self._errors['email'] = self.error_class("error")
                elif not user:
                    self._errors['password'] = self.error_class([
                            "Password you entered is incorrect."])
            else:
                self._errors['email'] = self.error_class([
                        "This email is not registered with Instahyre."])

        return cleaned_data



#registration is not properly validated
class RegistrationForm(forms.Form):
    pass

"""
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('first_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if (email and password and name):
            db_user_query = User.objects.filter(email=email)
            if db_user_query:
                raise forms.ValidationError("User with email is already exists")
        else:
            raise forms.ValidationError(" Please enter proper details")

        return cleaned_data
"""