from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from masterdata.models import Cliente, Zona, Operatore
from pickup.models import DailyItinerary
from .serializers import (
    ClienteSerializer,
    ZonaSerializer,
    OperatoreSerializer,
    DailyItinerarySerializer,
    ClienteRitiroSerializer,
)


class ClienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]


class ZonaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer
    permission_classes = [AllowAny]


class OperatoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Operatore.objects.all()
    serializer_class = OperatoreSerializer
    permission_classes = [AllowAny]


class ZoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer
    permission_classes = [AllowAny]


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


class RitiriDelGiornoAPIView(generics.ListAPIView):
    """
    Restituisce l'elenco dei clienti suggeriti per il ritiro del giorno,
    basato sul calcolo dei giorni trascorsi dall'ultimo ritiro e le tolleranze.
    """

    serializer_class = ClienteRitiroSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Cliente.objects.ritiri_del_giorno()
