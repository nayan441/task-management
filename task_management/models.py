from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)  
    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['mobile', 'username']  

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    users = models.ManyToManyField(User, related_name='user_tasks')

    def __str__(self):
        return str(id) + " - " + self.name    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
