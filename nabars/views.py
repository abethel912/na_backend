from .models import Nabars
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NabarsSerializer


class NabarsViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Nabars.objects.all()
    # The serializer class for serializing output
    serializer_class = NabarsSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]
