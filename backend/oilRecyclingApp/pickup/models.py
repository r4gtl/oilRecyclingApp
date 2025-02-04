from django.db import models
from masterdata.models import Cliente, Operatore
from django.contrib.auth.models import User


class Pickup(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pickups")
    operatore = models.ForeignKey(Operatore, on_delete=models.CASCADE, related_name="pickups")
    # Data prevista per il ritiro (può essere utile per confronti)
    scheduled_date = models.DateField()
    # Data e ora effettiva in cui il ritiro è stato effettuato
    actual_pickup_datetime = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, related_name="pickups", null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ritiro di {self.cliente.name} effettuato da {self.operatore.name} il {self.actual_pickup_datetime}"

