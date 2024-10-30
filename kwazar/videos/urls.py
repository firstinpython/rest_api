from django.urls import path
from .views import ListVideos, SpecificVideo

urlpatterns = [
    path("full_videos/",ListVideos.as_view(),name = "full_videos"),
    path("video/<int:pk>/",SpecificVideo.as_view(),name = "video")
]