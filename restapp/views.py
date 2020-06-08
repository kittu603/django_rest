from django.shortcuts import render
from .serializers import TaskSerializers,UserSerializer
from rest_framework import viewsets
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated,AllowAny #Allows access only to authenticated users.
#Allowany gives access to anyone to register for new class i.e.,CreateUserView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Provides generic filtering backends that can be used to filter the results returned by list views.
from rest_framework import filters
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) #class is access restricted to other than authenticated users
    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializers
    #below code using django filters
    # these are need for filtering to work,can be defined in settings also if not here
    #http://127.0.0.1:8000/task/?is_completed=False gives due tasks and viceversa
    # search filter enables to return back a specific match based on search_fields
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter , filters.SearchFilter)
    filter_fields = ('is_completed',)  #by which field u want to filter
    #ordering = ('date_created')   #can be used like this as well
    search_fields = ('task_name',)    #?search=Django gives that specific task obj with contains django in taskname


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer



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
