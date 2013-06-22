from django.conf.urls import patterns, include, url
# Cuando usamos otro servidor que no sea el de django agregamos la siguiente linea
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$','core.views.lista_propiedades'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cuentas/', include('authtools.urls')),
)

# Cuando usamos otro servidor que no sea el de django
urlpatterns += staticfiles_urlpatterns()