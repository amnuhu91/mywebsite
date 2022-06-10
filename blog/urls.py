from django.urls import path,include

from blog.views import (
    PostListView,
    PostDetailView,
    PostShareView,
    AddBlog
)
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<str:category>/', PostListView.as_view(), name='post_list_cat'),
    path('tag/<slug:tag_slug>/', PostListView.as_view(),
         name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         PostDetailView.as_view(), name='post_detail'),
    path('<int:post_id>/share/', PostShareView.as_view(), name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('new-post/', AddBlog.as_view(), name='new-post'),
    #path('ckeditor/', include('ckeditor_uploader.urls')),
]
