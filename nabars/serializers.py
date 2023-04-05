from .models import Nabars
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Nabars
        # the fields that should be included in the serialized output
        fields = ['name', 'img', 'address', 'description', 'website']