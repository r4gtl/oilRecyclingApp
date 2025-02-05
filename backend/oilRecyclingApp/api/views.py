from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from masterdata.models import Cliente, Zona, Operatore
from .serializers import (
    ClienteSerializer,
    ZonaSerializer,
    OperatoreSerializer,
    DailyItinerarySerializer,
)


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


class DailyItineraryAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = DailyItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Recupera o crea l'itinerario per l'operatore e per la data odierna
        operator = self.request.user
        oggi = timezone.localdate()
        itinerary, created = DailyItinerary.objects.get_or_create(
            operator=operator, date=oggi
        )
        # Se appena creato, potresti volerlo pre-popolare con i suggerimenti:
        if created:
            suggested_clienti = Cliente.objects.ritiri_del_giorno()
            itinerary.clienti.set(suggested_clienti)
        return itinerary
