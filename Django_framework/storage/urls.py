from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('download/', views.StorageDownloadView.as_view(), name = None)
    ]