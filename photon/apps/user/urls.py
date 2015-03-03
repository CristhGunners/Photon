from django.conf.urls import patterns, url
from .views import Detail_User, Logout

urlpatterns = patterns(
    '',
    url(r'^logout/$', Logout, name='logout'),
    url(r'^(?P<slug_user>[-\w\ ]+)/$', Detail_User.as_view(), name='detail'),
)
