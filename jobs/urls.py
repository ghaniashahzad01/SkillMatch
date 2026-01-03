from django.urls import path
from .views import create_job, edit_job, toggle_job_status, delete_job

urlpatterns = [
    path('create/', create_job, name='job-create'),
    path('edit/<int:job_id>/', edit_job, name='job-edit'),
    path('toggle/<int:job_id>/', toggle_job_status, name='job-toggle'),
    path('delete/<int:job_id>/', delete_job, name='job-delete'),
]
