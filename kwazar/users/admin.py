from django.contrib import admin

from users.models import MyUser,Category_course

admin.site.register(MyUser)
admin.site.register(Category_course)