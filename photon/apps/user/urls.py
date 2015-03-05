from django.conf.urls import patterns, url
from .views import Detail_User, Logout, Login, Signup, Settings

urlpatterns = patterns(
    '',
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^logout/$', Logout, name='logout'),
    url(r'^settings/$', Settings.as_view(), name='settings'),
    url(r'^(?P<slug_user>[-\w\ ]+)/$', Detail_User.as_view(), name='detail'),
)
