from django.utils.encoding import smart_str
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User


@receiver(pre_save, sender=User)
def add_slug(sender, instance, **kwargs):
    slug = str(smart_str(instance.username))
    instance.slug = slugify(slug)
