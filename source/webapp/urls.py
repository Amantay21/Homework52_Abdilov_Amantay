from django.urls import path
from webapp.views.task_views import TaskCreateView, \
    IndexView, TaskView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/add/', TaskCreateView.as_view(), name='tasks_create'),
    path('task/<int:pk>', TaskView.as_view(), name='tasks_view'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete')
]