# api/serializers.py
from rest_framework import serializers
from masterdata.models import Cliente, Zona, Operatore

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'
        
class OperatoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operatore
        fields = '__all__'
