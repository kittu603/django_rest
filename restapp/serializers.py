from .models import Task
from rest_framework import serializers
# Return the User model that is active in this project.
from django.contrib.auth import get_user_model


#creating a serializer for user model (l 4)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    #get access to user model and create an user depending upon provided username and pass
    #below method will be called when user is created i.e.,a POST is sent
    def create(self,validated_data):
        user = get_user_model().objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    #below shows the username and password to fill from auth user when /register triggered
    class Meta:
        model = get_user_model()
        fields = ('username','password') #which fields to show

#isAuthenicated checks the username and pass in Db and allows them in automatically


# serializers are used to convert models data to JSON
# remeber every rest API shld give data in JSON

class TaskSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(use_url = True)   #modifying image serializer setting here to show image url

    class Meta:
        model = Task   #which data table to pass to serializer
        fields = '__all__'

