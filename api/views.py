from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Todo, Post, Comment
from .serializers import UserSerializer, TodoSerializer, PostSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class UserTodoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Todo.objects.filter(userId=self.kwargs['user_pk'])
    serializer_class = TodoSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class UserPostViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Post.objects.filter(userId=self.kwargs['user_pk'])
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class PostCommentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Comment.objects.filter(postId=self.kwargs['post_pk'])
    serializer_class = CommentSerializer