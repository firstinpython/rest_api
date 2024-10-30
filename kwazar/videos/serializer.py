from rest_framework import serializers
from .models import VideosModel

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideosModel
        fields = "__all__"