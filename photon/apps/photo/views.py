# encoding:utf-8
# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from photon.apps.photo.models import Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


class Home(ListView):
    template_name = "photo/home.html"
    context_object_name = "photos"

    def get_queryset(self):
        photos_all = Photo.objects.filter(is_active=True).order_by(
            '-date_creation')
        paginator = Paginator(photos_all, 6)
        page = self.request.GET.get('page')
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
        return photos


class List_Tags(TemplateView):
    template_name = "photo/tags.html"


class Detail_Tag(DetailView):
    template_name = "photo/tag.html"
    model = Tag
    context_object_name = "tag"

    def get_object(self):
        return get_object_or_404(Tag, slug=self.kwargs['slug_tag'])

    def get_context_data(self, **kwargs):
        context = super(Detail_Tag, self).get_context_data(**kwargs)
        tag = self.get_object()
        photos_all = Photo.objects.filter(
            tags__name__in=[tag.name], is_active=True).order_by(
            '-date_creation')
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


class Download_Photo(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        photo = get_object_or_404(Photo, id=self.kwargs['id_photo'])
        photo.update_download_counter()
        self.url = photo.get_path_file()
        return super(Download_Photo, self).get_redirect_url(*args, **kwargs)
