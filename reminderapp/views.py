from rest_framework import generics
from .serializers import RemSerializer
from.models import reminder

# Create your views here.

class remcreateview(generics.CreateAPIView):
    queryset = reminder.objects.all()
    serializer_class = RemSerializer

class remlist(generics.ListAPIView):
    queryset = reminder.objects.all()
    serializer_class = RemSerializer