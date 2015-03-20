from django.conf.urls import patterns, url
from .views import Home, List_Tags, Detail_Tag, Download_Photo, Views_Photo, Upload, Delete_Photo

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^upload/$', Upload.as_view(), name='upload'),
    url(r'^tags/$', List_Tags.as_view(), name='tags'),
    url(r'^tags/(?P<slug_tag>[-\w\ ]+)/$', Detail_Tag.as_view(), name='tag'),
    url(r'^photo/download/(?P<id_photo>\d+)/$',
        Download_Photo.as_view(), name='download'),
    url(r'^photo/views/(?P<id_photo>\d+)/$',
        Views_Photo.as_view(), name='views'),
    url(r'^photo/delete/(?P<id_photo>\d+)/$',
        Delete_Photo.as_view(), name='delete'),
)
