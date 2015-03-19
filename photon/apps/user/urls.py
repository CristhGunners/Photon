from django.conf.urls import patterns, url
from .views import Detail_User, Settings, Crop

urlpatterns = patterns(
    '',
    url(r'^crop-avatar/$', Crop.as_view(), name='crop'),
    url(r'^settings/$', Settings.as_view(), name='settings'),
    url(r'^(?P<user>[-\w\ ]+)/$', Detail_User.as_view(), name='detail'),
)
