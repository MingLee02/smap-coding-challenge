from django.conf.urls import url

from . import views
from .models import Consumption

urlpatterns = [
    url(r'^$', views.summary.as_view(), name='summary'),
    url(r'^detail/(?P<user_id>\d+)$', views.detail.as_view(), name='detail'),
]