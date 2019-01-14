import django_filters

from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerialiser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerialiser
