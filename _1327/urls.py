from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('_1327',  # noqa
	url(r"^$", 'main.views.index', name='index'),
	url(r"^documents/", include('_1327.documents.urls', namespace='documents')),
	url(r"^minutes/", include('_1327.minutes.urls', namespace='minutes')),
	url(r"^login$", 'user_management.views.login', name='login'),
	url(r"^logout$", 'user_management.views.logout', name='logout'),
	url(r'^polls/', include('_1327.polls.urls', namespace='polls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r"^", include('_1327.information_pages.urls', namespace='information_pages')),
)
