from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cdi.views.home', name='home'),
    # url(r'^cdi/', include('cdi.foo.urls')),

    (r'^accounts/', include('allauth.urls')),
    (r'^events/', include('event.urls')),
    (r'^colleges/', include('college.urls')),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html'), name='account_profile'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^accounts/settings/$', 'cdi.views.settings', name='account_settings'),
    url(r'^admin/', include(admin.site.urls)),
)
