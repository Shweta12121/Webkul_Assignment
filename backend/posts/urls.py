from django.urls import path
from .views import (
    PostListCreateView,
    PostDeleteView,
    PostLikeView,
    PostDislikeView,
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:post_id>/delete/', PostDeleteView.as_view()),
    path('posts/<int:post_id>/like/', PostLikeView.as_view()),
    path('posts/<int:post_id>/dislike/', PostDislikeView.as_view()),
]
