from django.shortcuts import render
from .models import MyUser, Category_course
from .serializer import UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# class ListUsers(ListAPIView):
#     queryset = MyUser.objects.all()
#     serializer_class = UserSerializer

class ListUsers(APIView):
    def get(self, request, format=None):
        users = MyUser.objects.all()
        serializer = UserSerializer(users, many=True)
        for i in range(len(serializer.data)):
            res = Category_course.objects.filter(id=int(serializer.data[i]['course'])).first()
            if res is not None:
                serializer.data[i]['course'] = str(res.name)
        return Response(serializer.data)
