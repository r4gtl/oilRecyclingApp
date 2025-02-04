from django.shortcuts import render
from rest_framework.permissions import AllowAny

from rest_framework import generics
from masterdata.models import Cliente, Zona, Operatore
from .serializers import ClienteSerializer, ZonaSerializer, OperatoreSerializer


class ClienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]


class ZonaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer


class OperatoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Operatore.objects.all()
    serializer_class = OperatoreSerializer


class ZoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer


class ClienteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]
