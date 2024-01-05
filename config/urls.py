from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from api import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todos', views.TodoViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'todos',views.UserTodoViewSet, basename='users-todos')
users_router.register(r'posts',views.UserViewSet, basename='todos-posts')
#users_router.register(r'comments',views.PostViewSet, basename='posts-comments')



# Wire up our API using automatic URL routing.
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(users_router.urls)),
]

urlpatterns += router.urls

#users,todos,comments,posts