from django.shortcuts import render
import json

from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from tastypie.exceptions import ImmediateHttpResponse


from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse

import users.api

"""
def login(request):
    form_errors = {}
    if request.method == "POST":
        resource = users.api.UserLoginResource()
        try:
            resource.post_list(request=request)
            return redirect('/dashboard/')

        except ImmediateHttpResponse, e:
            form_errors = json.loads(e.response.content)['login']

    return render(request, "users/login.html",
                  {'form_errors': form_errors})

"""


def redirect_to_dashboard_if_loggedn(func):
    def _wrapped_func(*args, **kwargs):
        request = args[0]
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard/')
        return func(*args, **kwargs)

    return _wrapped_func


def get_user(username_or_email):
    try:
        return User.objects.get(email=username_or_email)
    except User.DoesNotExist:
        try:
            return User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            return None


@redirect_to_dashboard_if_loggedn
def simple_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        user = get_user(username_or_email)
        if user and authenticate(username=user.username, password=password):
            user = authenticate(username=user.username, password=password)
            django_login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'users/login.html', {'invalid': True})
    else:
        return render(request, 'users/login.html')    


def logout(request):
    auth_logout(request)
    return redirect('/')



def register(request):
    form_errors = {}
    if request.method == "POST":
        resource = users.api.RegistrationResource()
        try:
            resource.post_list(request=request)
            return redirect('/dashboard/')
        except ImmediateHttpResponse, e:
            form_errors = json.loads(e.response.content)['registration']
 
    return render(request, "users/register.html",
                   {'form_errors': form_errors})