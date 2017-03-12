from django.conf.urls import include, url
from . import views, feed

urlpatterns = [
    url(r'^$', views.PostIndex.as_view(), name='index'),
    url(r'^p/(?P<slug>\S+)/$', views.PostDetail.as_view(), name='post'),
    url(r'^t/(?P<slug>\S+)/$', views.TagIndex.as_view(), name='tag'),
    url(r'^feed/$', feed.PostsFeed(), name='feed'),
    url(r'^(?P<slug>\S+)/$', views.PageDetail.as_view(), name='page'),
]
