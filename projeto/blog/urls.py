from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.coment_list),
    url(r'^new/', views.new_post),
    url(r'^$', views.logar),
]
