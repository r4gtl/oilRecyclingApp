# api/serializers.py
from rest_framework import serializers
from masterdata.models import Cliente, Zona, Operatore
from pickup.models import DailyItinerary


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = "__all__"


class OperatoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operatore
        fields = "__all__"


class DailyItinerarySerializer(serializers.ModelSerializer):
    clienti = ClienteSerializer(many=True, read_only=True)
    clienti_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), write_only=True, many=True, source="clienti"
    )

    class Meta:
        model = DailyItinerary
        fields = ["id", "operatore", "date", "clienti", "clienti_ids"]
        read_only_fields = ["operator", "date"]
