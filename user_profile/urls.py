from django.conf.urls import url
from .views import users

urlpatterns = [
    url(r'^(?P<user_id>.+)/$', users, name='users'),
    url(r'^1', users, name='test'),
]
