from django.urls import path
from .views import (
    SignUpView, ProfileView, UserListView, UserDetailView, UserUpdateView,
    RoleCreateView, RoleListView, UserActivityLogListView
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/new/', RoleCreateView.as_view(), name='role_new'),
    path('activity_logs/', UserActivityLogListView.as_view(), name='user_activity_log_list'),
]
