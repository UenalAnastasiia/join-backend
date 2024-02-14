from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from contacts.views import ContactDetailsViewSet, ContactViewSet
from login.views import LoginView, Logout
from tasks.views import TaskDetailsViewSet, TaskViewSet
from users.views import UserDetailsViewSet, UsersViewSet


urlpatterns = [
    path('', lambda request: redirect('tasks/', permanent=True)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', Logout.as_view()),
    path('tasks/', TaskViewSet.as_view()),
    path('tasks/<int:pk>/', TaskDetailsViewSet.as_view()),
    path('users/', UsersViewSet.as_view()),
    path('users/<int:pk>/', UserDetailsViewSet.as_view()),
    path('contacts/', ContactViewSet.as_view()),
    path('contacts/<int:pk>/', ContactDetailsViewSet.as_view()),
]