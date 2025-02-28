from django.urls import path
from .views import get_jobs, job_detail

urlpatterns = [
    path('jobs/', get_jobs, name='job-list'),
    # path('jobs/<str:job_id>/', job_detail, name='job_detail'),
]
