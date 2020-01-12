from attachments.views import upload_file, download_file
from django.urls import path

urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    path('download_file/', download_file, name='download_file'),
    path('download_file/<str:key>/', download_file, name='download_file')
]
