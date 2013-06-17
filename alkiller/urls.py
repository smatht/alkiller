from django.conf.urls import patterns, include, url
# Cuando usamos otro servidor que no sea el de django agregamos la siguiente linea
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# Cuando usamos otro servidor que no sea el de django
urlpatterns += staticfiles_urlpatterns()