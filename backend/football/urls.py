from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
