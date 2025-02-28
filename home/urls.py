from django.urls import path
from .views import home_page, job_detail

urlpatterns = [
    path('', home_page, name='home'),
    path('jobs/<str:job_id>/', job_detail, name='job_detail'),  # Job detail page
]
