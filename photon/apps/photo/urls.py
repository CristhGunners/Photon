from django.conf.urls import patterns, url
from .views import Home

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    # url(r'^create/$', Create_Entry.as_view(), name='create'),
    # url(r'^delete/(?P<id_post>[-\w\ ]+)/$', Delete_Post.as_view(),
    #    name='delete'),
    # url(r'^(?P<slug_user>[-\w\ ]+)/(?P<slug_entry>[-\w\ ]+)/$',
    #   Detail_Entry.as_view(), name='entry-detail'),
)
