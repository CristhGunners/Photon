from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from .models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from photon.apps.photo.models import Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def Logout(request):
    logout(request)
    return redirect('/')


class Detail_User(DetailView):
    template_name = "user/user.html"
    models = User
    context_object_name = "profile"

    def get_object(self):
        return get_object_or_404(User, slug=self.kwargs['slug_user'])

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
