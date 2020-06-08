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
from restapp.views import TaskViewSet,CreateUserView#TasksCompletedViewSet,TasksDueViewSet
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
    path('',include(router.urls)),
    path('register/',views.CreateUserView.as_view(), name = 'user'),
    
    #We can add a login view for use with the browsable API, by editing the URLconf
    #The 'api-auth/' part of pattern can actually be whatever URL you want to use.
    #Now if you open up the browser again and refresh the page you'll see a 'Login' link in the top right of the page.
    
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)    #this is for loading media iamges


#settings.MEDIA_URL from django settings gives /media/
#settings.MEDIA_ROOT gives MEDIA_ROOT = os.path.join(BASE_DIR,'media')
