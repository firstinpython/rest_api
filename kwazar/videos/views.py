from django.shortcuts import render
from .models import VideosModel
from .serializer import VideoSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class ListVideos(APIView):

    def get(self, request, format=None):
        videos = VideosModel.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class SpecificVideo(RetrieveAPIView):
    queryset = VideosModel.objects.all()
    serializer_class = VideoSerializer

