from django.conf.urls import url
from django.conf import settings

from . import views
from .models import Consumption

urlpatterns = [
    url(r'^$', views.summary.as_view(), name='summary'),
    url(r'^detail/(?P<pk>\d+)$', views.detail.as_view(), name='detail'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
