from django.db import models


# Create your models here.
# created a model fto save to-do list
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_detail = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    #when a image is uploaded, it creates a images dir in MEDIA dir
    image = models.ImageField(upload_to= 'images/', default = 'noImg.jpg' )  



