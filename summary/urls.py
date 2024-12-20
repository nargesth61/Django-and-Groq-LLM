from django.urls import path
from .views import UploadFileAPIView, FileHistoryAPIView

urlpatterns = [
   path('upload/', UploadFileAPIView.as_view(), name='upload-file'),
    path('history/', FileHistoryAPIView.as_view(), name='file-history'),
]