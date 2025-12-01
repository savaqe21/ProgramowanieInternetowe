from django.urls import path
from . import views

urlpatterns = [
    path('ui/', views.todo_frontend_view, name='todo_frontend'),

    path('tasks/', views.tasks_view),
    path('tasks/<int:task_id>/done/', views.task_done),
    path('tasks/<int:task_id>/', views.task_delete),
]