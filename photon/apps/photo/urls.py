from django.conf.urls import patterns, url
from .views import Home, List_Tags, Detail_Tag

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tags/$', List_Tags.as_view(), name='tags'),
    url(r'^tags/(?P<slug_tag>[-\w\ ]+)/$', Detail_Tag.as_view(), name='tag'),
    # url(r'^create/$', Create_Entry.as_view(), name='create'),
    # url(r'^delete/(?P<id_post>[-\w\ ]+)/$', Delete_Post.as_view(),
    #    name='delete'),
    # url(r'^(?P<slug_user>[-\w\ ]+)/(?P<slug_entry>[-\w\ ]+)/$',
    #   Detail_Entry.as_view(), name='entry-detail'),
)
