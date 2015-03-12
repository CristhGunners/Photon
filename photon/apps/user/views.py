# encoding:utf-8
# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from photon.apps.photo.models import Photo
from .forms import Form_Settings_User
from .models import User


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
        paginator = Paginator(photos_all, 6)
        page = self.request.GET.get('page')
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
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
