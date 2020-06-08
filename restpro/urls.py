"""restpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from restapp.views import TaskViewSet#TasksCompletedViewSet,TasksDueViewSet
from django.conf.urls.static import static
from django.conf import settings
from restapp import views

router = routers.DefaultRouter()   # defaultrouter gives default page for route '/'
router.register('task', views.TaskViewSet)
'''
using simple router for classbase views
router = routers.SimpleRouter()
router.register('task',TaskViewSet)
router.register('tasks-due',TasksDueViewSet)
router.register('tasks-done',TasksCompletedViewSet)
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)    #this is for loading media iamges


#settings.MEDIA_URL from django settings gives /media/
#settings.MEDIA_ROOT gives MEDIA_ROOT = os.path.join(BASE_DIR,'media')
