from django.conf.urls import patterns, url
from .views import Detail_User, Settings

urlpatterns = patterns(
    '',
    url(r'^settings/$', Settings.as_view(), name='settings'),
    url(r'^(?P<slug_user>[-\w\ ]+)/$', Detail_User.as_view(), name='detail'),
)
