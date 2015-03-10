# encoding:utf-8
# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, RedirectView, CreateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from photon.apps.photo.models import Photo
from .forms import Form_Photo


class Upload(CreateView):
    template_name = "photo/upload.html"
    form_class = Form_Photo
    model = Photo
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Upload, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(Upload, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


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


class Download_Photo(View):

    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, id=self.kwargs['id_photo'])
        photo.update_download_counter()
        response = HttpResponse(
            photo.image, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % photo.image.name
        return response


class Views_Photo(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        photo = get_object_or_404(Photo, id=self.kwargs['id_photo'])
        photo.update_views_counter()
        self.url = photo.get_path_file()
        return super(Views_Photo, self).get_redirect_url(*args, **kwargs)
