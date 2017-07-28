from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.coment_list),
    url(r'^new/', views.new_post),
    url(r'^$', views.logar),
    url(r'user_new/', views.user_new),
    url(r'^post/(?P<pk>[0-9]+)/edit/', views.edit_post),
    url(r'^post/(?P<pk>[0-9]+)/delete/', views.delete_post),
    url(r'^logout/', views.logout_user),
]
