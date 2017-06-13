from django.conf.urls import url
from .views import PasswordListView

urlpatterns = [
    url(r'^$', PasswordListView.as_view(), name='article-list'),
]