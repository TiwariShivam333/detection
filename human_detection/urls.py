from django.urls import path
from . import human
# from . import views

urlpatterns = [
    path('detect/', human.new_function),
]
