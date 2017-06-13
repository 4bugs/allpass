from django.conf.urls import url
from .views import RegisterView, register_ok

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register_ok/$', register_ok, name='register_ok'),
]