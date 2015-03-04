from django.conf.urls import patterns, url
from .views import Home, List_Tags, Detail_Tag, Download_Photo

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tags/$', List_Tags.as_view(), name='tags'),
    url(r'^tags/(?P<slug_tag>[-\w\ ]+)/$', Detail_Tag.as_view(), name='tag'),
    url(r'^photo/download/(?P<id_photo>\d+)/$',
        Download_Photo.as_view(), name='download'),
)
