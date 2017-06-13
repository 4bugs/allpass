from django.conf.urls import url
from .views import users

urlpatterns = [
    url(r'^(?P<user_id>.+)/$', users),
]
