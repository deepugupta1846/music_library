
from django.contrib import admin

from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('delete/<int:id>/', delete),
    path('playsong/<int:id>/', playMusic),
    path('playbyid/<int:id>/', showDataById)
]
