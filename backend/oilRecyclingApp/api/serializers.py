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


class ClienteRitiroSerializer(serializers.ModelSerializer):
    # Un campo che restituisce l'ultimo ritiro effettuato
    ultimo_ritiro = serializers.DateTimeField(
        source="last_pickup_datetime", read_only=True
    )

    class Meta:
        model = Cliente
        fields = [
            "id",
            "ragionesociale",
            "indirizzo",
            "cap",
            "city",
            "provincia",
            "sito_web",
            "e_mail",
            "pickup_date",
            "tolerance_before",
            "tolerance_after",
            "ultimo_ritiro",
        ]
