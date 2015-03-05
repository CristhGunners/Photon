# encoding:utf-8
# -*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Photo(models.Model):
    image = models.ImageField(upload_to='photo')
    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    download_count = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    tags = TaggableManager()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    def get_path_file(self):
        ruta = settings.MEDIA_URL+'%s' % (self.image.name)
        return ruta

    def update_download_counter(self):
        self.download_count = self.download_count+1
        self.save()

    def update_views_counter(self):
        self.views = self.views+1
        self.save()
