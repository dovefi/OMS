from django.conf.urls import url

from . import views

# namespace oms - Usage  oms:index
app_name = 'oms'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateUserView.as_view(), name='create_user'),
    url(r'^create2/$', views.CreateUser, name='create')
]