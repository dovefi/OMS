from django.conf.urls import url

from . import views

# namespace oms - Usage  oms:index
app_name = 'oms'

urlpatterns = [
    # CBV
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateUserView.as_view(), name='create_user'),
    url(r'^login/$', views.LoginUserView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutUserView.as_view(), name='logout'),

    # FBV
    url(r'^create2/$', views.CreateUser, name='create'),
]

