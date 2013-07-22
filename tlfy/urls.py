from django.conf.urls import patterns, include, url
from os.path import dirname, join

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

media = join(
	dirname(dirname(__file__)), 'media'
)

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
    url(r'^create_news/$', 'news.views.create_news'),
    url(r'^news/(?P<nid>\d+)/$', 'news.views.news_page'),
    url(r'^news/all/$', 'news.views.all_news'),
    url(r'^create_intro/$', 'news.views.create_intro'),
    url(r'^intro/all/$', 'news.views.all_intro'),
    url(r'^create_law/$', 'news.views.create_law'),
    url(r'^law/all/$', 'news.views.all_law'),
    url(r'^create_train/$', 'news.views.create_train'),
    url(r'^train/all/$', 'news.views.all_train'),

    url(r'^message/write/$', 'message.views.write_page'),
    url(r'^message/(?P<mid>\d+)/$', 'message.views.message_page'),
    url(r'^message/inbox/$', 'message.views.inbox'),
    #url(r'^message/set_read/(?P<mid>\d+)/$', 'message.views.set_read'),
    #url(r'^message/delete/(?P<mid>\d+)/$', 'message.views.delete'),

    url(r'^create_notice/$', 'notice.views.create_notice'),
    url(r'^notice/all/$', 'notice.views.all_notice'),

    url(r'^create_doc_example/$', 'doc_example.views.create_doc_example'),
    url(r'^doc_example/all/$', 'doc_example.views.all_doc_example'),

	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':media}),
)
