from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TaskSerializer, UserSerializer, AssignTaskSerializer
from .models import Task, User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserList(APIView):
    @swagger_auto_schema(
        operation_summary="List all users",
        operation_description="Retrieve a list of all users excluding staff and superusers.",
        responses={200: UserSerializer(many=True)}
    )
    def get(self, request,):
        try:
            users = User.objects.filter(is_staff=False, is_superuser=False)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_summary="Create a new user",
        operation_description="Create a user with the required fields.",
        request_body=UserSerializer,  # Specify request body for POST
        responses={201: UserSerializer}
    )   
    def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetOrUpdateUser(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a user by ID",
        operation_description="Fetch details of a user by their ID, excluding staff and superusers.",
        responses={200: UserSerializer, 404: "User not found"}
    )
    def get(self, request, pk):
        try:
            users = User.objects.get(pk=pk,  is_staff=False, is_superuser=False)
            serializer = UserSerializer(users)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        operation_summary="Update a user",
        operation_description="Partially update a user's details.",
        request_body=UserSerializer,  # Specify request body for PATCH
        responses={200: UserSerializer, 400: "Invalid data", 404: "User not found"}
    )
    def patch(self, request, pk):
        try:
            user = User.objects.get(pk=pk, is_staff=False, is_superuser=False)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        operation_summary="Delete a user",
        operation_description="Delete a user by their ID.",
        responses={204: "User deleted successfully", 404: "User not found"}
    )   
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk, is_staff=False, is_superuser=False)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
# @api_view(['GET'])
# def get_user(self, request, pk):
#     try:
#         users = User.objects.get(pk=pk,  is_staff=False, is_superuser=False)
#         serializer = UserSerializer(users)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except User.DoesNotExist:
#         return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
    

    
# @api_view(['PATCH'])
# def update_user(self, request, pk):
#     try:
#         user = User.objects.get(pk=pk, is_staff=False, is_superuser=False)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except User.DoesNotExist:
#         return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
# @api_view(['DELETE'])      
# def delete_user(self, request, pk):
#     try:
#         user = User.objects.get(pk=pk, is_staff=False, is_superuser=False)
#         user.delete()
#         return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#     except User.DoesNotExist:
#         return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

class TaskList(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                task = Task.objects.get(pk=pk)
                serializer = TaskSerializer(task)
            else:
                tasks = Task.objects.all()
                serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, )
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response({"message": "Task deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='post',
    request_body=TaskSerializer,
    responses={201: TaskSerializer},
    operation_summary="Create task",
    operation_description="Create a new task"
)
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='PATCH',
    request_body=TaskSerializer,
    responses={201: TaskSerializer},
    operation_summary="Update task",
    operation_description="Update an existing task"
)
@api_view(['PATCH'])
def update_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(
    method='get',
    responses={200: TaskSerializer},
    operation_summary="Get user tasks",
    operation_description="Get all tasks assigned to a user"
)   
@api_view(['GET'])
def get_user_task(request, pk):
    try:
        tasks = Task.objects.filter(users=pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

     
@swagger_auto_schema(
    method='post',
    manual_parameters=[
        openapi.Parameter('task_id', openapi.IN_QUERY, description="Task ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('user_ids', openapi.IN_QUERY, description="List of User IDs", type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER))
    ],
    operation_summary="Assign task",
    operation_description="Assign a task to one or more users",
    responses={200: "Task assigned successfully"}
)
@api_view(['POST'])
def assign_task(request):
        user_id = request.data.get('user_id', [])
        task_id = request.data.get('task_id', None)
        if not task_id:
            return Response({"message": "Task ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not user_id:
            return Response({"message": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = Task.objects.filter(id = task_id).first()
        already_assigned = instance.users.filter(id__in=user_id).values_list('id', flat=True)
        if already_assigned:
            message = f"User with ID: {', '.join(map(str, already_assigned))}  already assigned to this task."
        else:
            instance.users.add(*user_id)  
            instance.save()
            message =f"Task assigned successfully"
        return Response({"message":message}, status=status.HTTP_201_CREATED)
