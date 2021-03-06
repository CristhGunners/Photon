# encoding:utf-8
# -*- encoding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import title
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from photon.apps.photo.models import Photo


class UserManager(BaseUserManager):

    def _create_user(
        self, username, email, password, is_staff, is_superuser,
            **extra_fields):

        email = self.normalize_email(email)
        user = self.model(
            username=username, email=email, is_active=True, is_staff=is_staff,
            is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(
            username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(
            username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='author')
    website = models.URLField(blank=True)

    # Redes Sociales

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    googleplus = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    objects = UserManager()

    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    def full_name(self):
        if self.first_name or self.last_name:
            return title('%s %s' % (self.first_name, self.last_name))
        else:
            return title(self.username)

    def get_absolute_url(self):
        return reverse('user:detail', args=(self.username,))

    def get_photo_count(self):
        return Photo.objects.filter(
            user=self, is_active=True).count()


class TmpImage(models.Model):
    image = models.ImageField(upload_to="tmp")

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(TmpImage, self).delete(*args, **kwargs)
