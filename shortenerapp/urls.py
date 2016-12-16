from django.conf.urls import url
from .views import url_redirect, home, success


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^success/(?P<shortcode>[\w-]+)/$', success, name='success'),
    url(r'^(?P<shortcode>[\w-]+)/$', url_redirect, name='url_redirect'),
]
