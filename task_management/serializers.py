from rest_framework import serializers
from .models import Task, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'completed_at', 'status',]
        read_only_fields = ['created_at','users']

class AssignTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'users']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',  'username', 'first_name', 'last_name', 'email', 'mobile']