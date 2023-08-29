from django.urls import path
from .views import PostList, PostDetail, CategoryList, PostListProv, PostCreateProv, PostDetailProv, PostDeleteProv

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<id>/', PostDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('affiliate/posts/', PostListProv.as_view()),
    path('affiliate/posts/create/', PostCreateProv.as_view()),
    path('affiliate/posts/<id>/', PostDetailProv.as_view()),
    path('affiliate/posts/<id>/delete/', PostDeleteProv.as_view()),
]
