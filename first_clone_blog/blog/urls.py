from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^about/$', views.aboutView.as_view(), name = 'about'),
    url(r'^$', views.postListView.as_view(), name = 'post_list'),
    url(r'^post/(?P<pk>\d+)$', views.postDetailView.as_view(), name = 'post_detail'),
    url(r'^post/new/$', views.postCreateView.as_view(), name = 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.postUpdateView.as_view(), name = 'post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.postDeleteView.as_view(), name = 'post_remove'),
    url(r'^drafts/$', views.draftListView.as_view(), name = 'post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name = 'add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name = 'comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name = 'comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name = 'post_publish'),
]
