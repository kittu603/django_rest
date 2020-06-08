from django.shortcuts import render
from .serializers import TaskSerializers
from rest_framework import viewsets
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend

# Provides generic filtering backends that can be used to filter the results returned by list views.
from rest_framework import filters
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializers
    #below code using django filters
    # these are need for filtering to work,can be defined in settings also if not here
    #http://127.0.0.1:8000/task/?is_completed=False gives due tasks and viceversa
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('is_completed',)  #by which field u want to filter
    #ordering = ('date_created')   #can be used like this as well


'''

instead of creating each view for each type of filter, we can use django_filters as above

#view for completed tasks - API endpoint for completed tasks

class TasksCompletedViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(is_completed = True)
    serializer_class = TaskSerializers

#view for completed tasks  - API endpoint for due tasks

class TasksDueViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(is_completed = False)
    serializer_class = TaskSerializers
'''
