from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todos', views.TodoViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
users_router = routers.NestedSimpleRouter(router, r'users', lookup='users')
users_router.register(r'todos',views.TodoViewSet, basename='users-todos')
users_router.register(r'posts',views.TodoViewSet, basename='todos-posts')
users_router.register(r'comments',views.TodoViewSet, basename='posts-comments')



# Wire up our API using automatic URL routing.
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += router.urls

#users,todos,comments,posts