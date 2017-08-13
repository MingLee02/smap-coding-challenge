from django.conf.urls import url

from . import views
from .models import Consumption

urlpatterns = [
    url(r'^$', views.summary.as_view(), name='summary'),
]