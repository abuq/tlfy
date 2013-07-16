from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tlfy.views.home', name='home'),
    # url(r'^tlfy/', include('tlfy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.main_page'),
    url(r'^userp/login/$', 'user_profile.views.log_in'),
    url(r'^userp/logout/$', 'user_profile.views.log_out'),
    url(r'^create_users/$', 'user_profile.views.create_users'),
)
