from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from photon.apps.user.views import RegistrationViewUniqueEmail
from photon.apps.system.views import System_403, System_404, System_500


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'photon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^accounts/password/reset/complete/$', auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^accounts/register/$', RegistrationViewUniqueEmail.as_view(),
                    name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', include('photon.apps.photo.urls', namespace="photo")),
    url(r'^', include('photon.apps.user.urls', namespace="user")),
)

handler403 = System_403.as_error_view()
handler404 = System_404.as_error_view()
handler500 = System_500.as_error_view()

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
