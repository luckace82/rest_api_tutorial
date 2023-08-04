from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer,GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API ENDPOINT THAT allows user to be viewed or edited"""
    queryset=User.objects.all().order_by('date_joined')
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    """API endpoimt that allows groiups to be viewed or edited
    """
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]
        