from django.shortcuts import render
# from django.http import Http404
# from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from rest_framework import status
from . import human
import psutil
import os
import signal
from subprocess import check_output

import requests



class DetectAPI(APIView):
    """For detecting human"""

    def get(self, request, format=None):
        """Returns API view"""

        return Response({'API: Run human detection'})

    serializer_class = serializers.DetectionSerializer

    def post(self, request):
        """Start the script"""
        # url = 'http://192.168.10.73:8000/human_detection/detect/'
        serializer = serializers.DetectionSerializer(data=request.data)

        if serializer.is_valid():
            on_off = serializer.data.get('checker')
            if on_off == "start":
                human.check_for_trespassers(on_off)
            if on_off == "stop":
                kill_process_id('python')
            m = 'Received {0}'.format(on_off)
            return Response({'message': m})

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # headers = {'content-type': 'application/json'}
        # params = {'handler': 'hello'}
        # requests.post(url, params=params, headers=headers)


# @api_view(["POST"])
def new_function(request):
    if request:
            print("Hello World")
    return HttpResponse("<h3>CODE EXECUTED</h3>")


def kill_process_id(process_name):
    """Get a list of all the PIDs of a all the running process whose name contains
    the given string processName"""

    pro_id = []

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            # Check if process name contains the given name string.
            if process_name.lower() in pinfo['name'].lower():
                pro_id.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in pro_id:
        if element['pid'] == os.getpid():
            print("not closing" + str(element['pid']))
        else:
            print("killing PID:" + str(element['pid']))
            os.kill(element['pid'], signal.SIGTERM)
