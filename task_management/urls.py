
from django.contrib import admin
from django.urls import path,  include
from . import views
urlpatterns = [
    path('users', views.UserList.as_view(), name='index'),
    path('users/<int:pk>/', views.GetOrUpdateUser.as_view(), name='index'),
    # path('users/<int:pk>/', views.update_user, name='index'),
    # path('users/<int:pk>/', views.delete_user, name='index'),
    
    # path('tasks', views.TaskList.as_view(), name='index'),
    # path('tasks/<int:pk>/', views.TaskList.as_view(), name='index'),

    path('tasks/<int:pk>/', views.get_user_task, name='get_user_task'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/update/', views.update_task, name='update_task'),
    path('tasks/assign/', views.assign_task, name='assign_task'),

]
