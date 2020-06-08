from .models import Task
from rest_framework import serializers


# serializers are used to convert models data to JSON
# remeber every rest API shld give data in JSON

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task   #which data table to pass to serializer
        fields = '__all__'

