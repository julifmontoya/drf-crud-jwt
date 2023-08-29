from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import PostListSerializer, PostSerializer, CategoryListSerializer
from .models import Post, Category
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from user.utils import has_permission


class PostListProv(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(user=user)


class PostCreateProv(APIView):
    permission_classes = (IsAuthenticated,)
 
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        user=self.request.user

        if request.user.is_verified:
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class PostDetailProv(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        user = self.request.user
        has_permission(post.user, user)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = get_object_or_404(Post, id=id)
        user= self.request.user
        has_permission(post.user, user)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

class PostDeleteProv(DestroyAPIView):  
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = ()


class PostDetail(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = ()
    lookup_field = 'id'


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = ()