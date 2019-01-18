from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from rest_framework import status
from . import human
import psutil
import os
import signal
import threading


def kill_process_id():
    """Get a list of all the PIDs of a all the running process whose name contains
    the given string processName"""
    process_name = 'Python'
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

    print(pro_id)

    for element in pro_id:
        if element['pid'] == os.getpid():
            print("Killing" + str(element['pid']))
            os.kill(element['pid'], signal.SIGTERM)

        # else:
        #     print("killing PID:" + str(element['pid']))
        #     os.kill(element['pid'], signal.SIGTERM)


t1 = threading.Thread(target=human.check_for_trespassers)
t2 = threading.Thread(target=kill_process_id)


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
                # t1 = threading.Thread(target=human.check_for_trespassers)
                t1.start()
                return Response({'Running human detection'})
            if on_off == "stop":
                # t2 = threading.Thread(target=kill_process_id)
                t2.start()
                return Response({'Stopping human detection'})

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # headers = {'content-type': 'application/json'}
        # params = {'handler': 'hello'}
        # requests.post(url, params=params, headers=headers)
