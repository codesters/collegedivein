from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
from event.views import EventUserListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cdi.views.home', name='home'),
    # url(r'^cdi/', include('cdi.foo.urls')),

    (r'^accounts/', include('allauth.urls')),
    (r'^events/', include('event.urls')),
    (r'^colleges/', include('college.urls')),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^accounts/profile/$', login_required(TemplateView.as_view(template_name='profile.html')), name='account_profile'),
    url(r'^accounts/events/$', login_required(EventUserListView.as_view()), name='account_events'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^accounts/settings/$', 'cdi.views.settings', name='account_settings'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^robots\.txt$', direct_to_template,
        {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {
        'url': '/media/images/favicon.ico'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
