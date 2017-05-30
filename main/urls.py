from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^poet/(?P<pk>\d+)/$', views.poet, name='poet'),
]

