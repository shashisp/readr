import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf.urls import url
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse

from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpBadRequest
from tastypie.utils import trailing_slash
from tastypie.validation import FormValidation
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource, Resource



import users.forms as forms


class UserLoginResource(ModelResource):
    """ A resource that logs a user in.
    """

    class Meta:
        resource_name = 'user_login'
        authentication = Authentication()
        list_allowed_methods = ['post']
        validation = FormValidation(form_class=forms.LoginForm)
        always_return_data = True
        excludes = ['password']

    def obj_create(self, bundle, **kwargs):
        """ Send errors if data is not valid else login the user.
        """

        if not self.is_valid(bundle):
            raise ImmediateHttpResponse(response=HttpBadRequest(
                json.dumps(bundle.errors)))

        user = authenticate(email=bundle.data["email"],
                            password=bundle.data["password"])
        login(bundle.request, user)

        properties = {
            "name": user.get_full_name()
        }

        return bundle

    def create_response(self, request, bundle, *args, **kwargs):


        if "password" in bundle.data:
            del bundle.data['password']

        bundle.data['nextUrl'] = reverse('dashboard')

        return super(UserLoginResource, self).create_response(
                request, bundle, *args, **kwargs)
