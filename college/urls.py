from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from college.views import CollegeListView, CollegeTypeListView, CollegeDetailView

urlpatterns = patterns('',
    # url(r'^$', 'cdi.views.home', name='home'),
    url(r'^$', CollegeListView.as_view(), name='college_all'),
     url(r'^type/(?P<slug>\w+)/$', CollegeTypeListView.as_view(), name='college_type'),
    url(r'^(?P<slug>\w+)/$', CollegeDetailView.as_view(), name='college_detail'),
    )
