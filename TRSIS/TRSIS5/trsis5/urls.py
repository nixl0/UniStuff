from django.contrib import admin
from django.urls import path
from imageproc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.image_upload),
]