from django.contrib import admin
from django.urls import path
from tasks.views import tasks
from login.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('tasks/', tasks, name='tasks'),
]
