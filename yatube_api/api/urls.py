from rest_framework.routers import DefaultRouter
from django.urls import include, path, re_path
from .views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/$',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comments-list',
    ),
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/(?P<pk>\d+)/$',
        CommentViewSet.as_view(
            {'get': 'retrieve', 'put': 'update',
                'patch': 'partial_update', 'delete': 'destroy'}
        ),
        name='comment-detail',
    ),
]
