from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('robust-secret-login/', admin.site.urls),
    path('', include('tracker.urls')),
]
