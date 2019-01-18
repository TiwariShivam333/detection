from rest_framework import serializers


class DetectionSerializer(serializers.Serializer):
    """Serializes the input"""

    checker = serializers.CharField(max_length=5)

