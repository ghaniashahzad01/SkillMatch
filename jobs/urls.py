from django.urls import path
from .views import create_job

urlpatterns = [
    path('create/', create_job, name='job-create'),
]
