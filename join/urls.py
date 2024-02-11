from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from login.views import LoginView
from tasks.views import TaskDetailsViewSet, TaskViewSet


urlpatterns = [
    path('', lambda request: redirect('tasks/', permanent=True)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('tasks/', TaskViewSet.as_view()),
    path('tasks/<int:pk>/', TaskDetailsViewSet.as_view())
]