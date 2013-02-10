from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cdi.views.home', name='home'),
    # url(r'^cdi/', include('cdi.foo.urls')),

    (r'^accounts/', include('allauth.urls')),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^accounts/profile/$', 'django.views.generic.simple.direct_to_template', {'template': 'profile.html' }, name="account_profile"),
    url(r'^accounts/settings/$', 'cdi.views.settings', name='account_settings'),
    url(r'^admin/', include(admin.site.urls)),
)
