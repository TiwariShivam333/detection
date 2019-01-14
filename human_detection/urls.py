from django.urls import path
from django.conf.urls import url
from . import human
from . import views

urlpatterns = [
    path('detect/', views.DetectAPI.as_view()),
]
