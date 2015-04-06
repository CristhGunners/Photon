from django.views.generic import TemplateView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def my_paginator(self, queryset):
    paginator = Paginator(queryset, 6)
    page = self.request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return photos


class BaseErrorView(View):

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()

        def view(request):
            r = v(request)
            r.render()
            return r

        return view


class System_403(BaseErrorView, TemplateView):
    template_name = "system/403.html"


class System_404(BaseErrorView, TemplateView):
    template_name = "system/404.html"


class System_500(BaseErrorView, TemplateView):
    template_name = "system/500.html"
