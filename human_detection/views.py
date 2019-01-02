# from django.shortcuts import render
# from django.http import Http404
# from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.http import HttpResponse
import sys


def index(request):
    return HttpResponse(
        "<h1> This is the detection app homepage.</h1>"
    )


# @api_view(["POST"])
def new_function(request):
    if request:
            print("Hello World")
    return HttpResponse("<h3>CODE EXECUTED</h3>")

