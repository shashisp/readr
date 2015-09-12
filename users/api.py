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
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields




import users.forms as forms


class UserLoginResource(ModelResource):
    """ A resource that logs a user in.
    """

    class Meta:
        resource_name = 'login'
        authentication = Authentication()
        list_allowed_methods = ['post']
        validation = FormValidation(form_class=forms.LoginForm)
        always_return_data = True
        excludes = ['password']

    def obj_create(self, bundle, **kwargs):

        if not self.is_valid(bundle):
            raise ImmediateHttpResponse(response=HttpBadRequest(
                json.dumps(bundle.errors)))

        user = authenticate(email=bundle.data["email"],
                            password=bundle.data["password"])
        login(bundle.request, user)

        return bundle

    def create_response(self, request, bundle, *args, **kwargs):

        if "password" in bundle.data:
            del bundle.data['password']

        bundle.data['nextUrl'] = reverse('dashboard')
        return super(UserLoginResource, self).create_response(
                request, bundle, *args, **kwargs)



class UserRegistrationResource(ModelResource):
    email = fields.CharField()
    name = fields.CharField()
    password = fields.CharField()

    class Meta:
        object_class = User
        resource_name = 'registration'
        validation = FormValidation(
                form_class=forms.RegistrationForm)
        list_allowed_methods = ['post']
        detail_allowed_methods = []
        authentication = Authentication()
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        bundle.obj = self._meta.object_class()
        
        bundle = self.full_hydrate(bundle)
        self.is_valid(bundle)

        if bundle.errors:
            raise ImmediateHttpResponse(response=self.error_response(
                bundle.request, bundle.errors))

        user = User.objects.create_user(
            username=bundle.data['email'][:30],
            password=bundle.data['password'],
            email=bundle.data['email'],
            first_name=bundle.data['first_name'],
            last_name=bundle.data['last_name'],
        )

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(bundle.request, user)

        return bundle

    def create_response(self, request, bundle, *args, **kwargs):


        if "password" in bundle.data:
            del bundle.data['password']

        bundle.data['nextUrl'] = reverse('dashboard')

        return super(UserRegistrationResource, self).create_response(
                request, bundle, *args, **kwargs)

