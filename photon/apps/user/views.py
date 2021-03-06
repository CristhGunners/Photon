# encoding:utf-8
# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from photon.apps.photo.models import Photo
from photon.apps.system.views import my_paginator

from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from easy_thumbnails.files import get_thumbnailer
from .forms import Form_Settings_User
from .models import User, TmpImage


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail


class Detail_User(DetailView):
    template_name = "user/user.html"
    models = User
    context_object_name = "profile"

    def get_object(self):
        return get_object_or_404(
            User, username__iexact=self.kwargs['user'])

    def get_context_data(self, **kwargs):
        context = super(Detail_User, self).get_context_data(**kwargs)
        photos_all = Photo.objects.filter(
            user=self.get_object(), is_active=True).order_by('-date_creation')
        photos = my_paginator(self, photos_all)
        context['photos'] = photos
        return context


class Settings(UpdateView):
    template_name = "user/settings.html"
    form_class = Form_Settings_User
    success_url = "/"
    model = User

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Settings, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(
            User, is_active=True, username__iexact=self.request.user.username)

    def get_initial(self):
        user = self.request.user
        data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'avatar': user.avatar,
            'last_name': user.last_name,
            'website': user.website,
            'facebook': user.facebook,
            'twitter': user.twitter,
            'googleplus': user.googleplus,
            'instagram': user.instagram,
        }
        return data

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save()
        self.success_url = self.object.get_absolute_url()
        return super(Settings, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Crop(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Crop, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        tmpImg = TmpImage()
        tmpImg.image = self.request.FILES['file']
        tmpImg.save()
        thumb_url = get_thumbnailer(tmpImg.image)['avatar'].url
        tmpImg.delete()
        return HttpResponse(thumb_url)
