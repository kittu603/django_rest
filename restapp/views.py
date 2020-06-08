from django.shortcuts import render
from .serializers import TaskSerializers
from rest_framework import viewsets
from .models import Task
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializers

#view for completed tasks

class TasksCompletedViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(is_completed = True)
    serializer_class = TaskSerializers

#view for completed tasks

class TasksDueViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(is_completed = False)
    serializer_class = TaskSerializers

