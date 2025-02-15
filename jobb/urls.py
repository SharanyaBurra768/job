
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('joblist.urls')), 
    path('home/', include('home.urls')), 
    path('users/', include('users.urls')), 
]