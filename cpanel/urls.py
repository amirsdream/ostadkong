from django.conf.urls import url, include
from . import views as views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
	url(r'^cpanel/$', views.cpanel, name='cpanel'),
	url(r'^cpanel/login/$', auth_views.login,{'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
	url(r'^cpanel/logout/$', auth_views.logout,{'next_page': 'login'}, name='logout'),
]

#poem urls
urlpatterns += [
    url(r'^cpanel/poem/$', views.PoemCreate.as_view(), name='poem'),
    url(r'^cpanel/editpoem/$', views.PoemList.as_view(), name='poem_edit'),
    url(r'^cpanel/(?P<pk>\d+)/updatepoem/$',views.PoemUpdate.as_view(), name='update_poem'),
    url(r'^cpanel/(?P<pk>\d+)/deletepoem/$',views.PoemDelete.as_view(), name='delete_poem'),
]