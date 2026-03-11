from django.urls import path
from .views import (
    StudentList, StudentDetail,
    ProjectList, ProjectDetail,
    TeamList, TeamDetail,
    TaskList, TaskDetail,
    AssignmentList, AssignmentDetail,
    StatusList, StatusDetail,UserCreate
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/',UserCreate.as_view(),name='create-user'),
    path('token/',TokenObtainPairView.as_view(),name='get-token'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh-token'),
    path('Student/', StudentList.as_view(), name='student-list'),
    path('api/Student/<str:pk>/', StudentDetail.as_view(), name='student-detail'),

    path('Project/', ProjectList.as_view(), name='project-list'),
    path('api/Project/<str:pk>/', ProjectDetail.as_view(), name='project-detail'),

    path('Team/', TeamList.as_view(), name='team-list'),
    path('api/Team/<int:pk>/', TeamDetail.as_view(), name='team-detail'),  

    path('Task/', TaskList.as_view(), name='task-list'),
    path('api/Task/<str:pk>/', TaskDetail.as_view(), name='task-detail'),

    path('Assignment/', AssignmentList.as_view(), name='assignment-list'),
    path('api/Assignment/<str:pk>/', AssignmentDetail.as_view(), name='assignment-detail'),

    path('Status/', StatusList.as_view(), name='status-list'),
    path('api/Status/<str:pk>/', StatusDetail.as_view(), name='status-detail'),
]