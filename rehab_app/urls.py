from rehab_app.views import *
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('portal.urls')),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),


    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
    
    # Admin
    (r'^admin/', include(admin.site.urls)),

    (r'^static_media_alex/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^.*/static_media_alex/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
