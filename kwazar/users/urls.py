from django.urls import path,include,re_path
from .views import ListUsers
urlpatterns = [
    path('',ListUsers.as_view()),
    # path('users/',include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]