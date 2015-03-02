from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Photo(models.Model):
    image = models.ImageField(upload_to='photo')
    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('photo:detail', kwargs={
            'slug_user': self.kwargs['slug_user'],
            'id_photo': self.kwargs['slug_user'],
            })
