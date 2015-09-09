from django.shortcuts import render
import json

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from tastypie.exceptions import ImmediateHttpResponse


import users.api


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


def logout(request):
    logout(request)
    return redirect(reverse('/'))
