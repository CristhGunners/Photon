from django.shortcuts import render
from django.views.generic import ListView
from photon.apps.photo.models import Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Home(ListView):
    template_name = "photo/home.html"
    context_object_name = "photos"

    def get_queryset(self):
        photos_all = Photo.objects.filter(is_active=True)
        paginator = Paginator(photos_all, 6)
        page = self.request.GET.get('page')
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
        return photos
