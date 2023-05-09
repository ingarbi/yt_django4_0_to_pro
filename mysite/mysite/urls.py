from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    #http://127.0.0.1:8000/hello/
    path("myapp/", include("myapp.urls", namespace="myapp"))
]
