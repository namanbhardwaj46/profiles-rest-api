from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField(min_value=18, max_value=100)
