# taskmanager/urls.py

from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.task_list, name='task_list'),  # URL raíz apunta a la vista task_list
    path('tasks/', include('tasks.urls')),  # Incluir las URLs del app tasks
]
