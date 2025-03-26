from rest_framework import serializers
from .models import Task, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description',]
        read_only_fields = ['created_at','users', 'status', 'completed_at']

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'completed_at', 'status',]
        read_only_fields = ['created_at','users']

class AssignTaskSerializer(serializers.ModelSerializer):
    user_id = serializers.ListField(
        child=serializers.IntegerField()
    )   
    task_id = serializers.IntegerField()
    class Meta:
        model = Task
        fields = ['task_id', 'user_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',  'username', 'first_name', 'last_name', 'email', 'mobile']