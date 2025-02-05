from django.db import models
from masterdata.models import Cliente, Operatore, Zona
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class Pickup(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="pickups"
    )
    operatore = models.ForeignKey(
        Operatore, on_delete=models.CASCADE, related_name="pickups"
    )
    # Data prevista per il ritiro (può essere utile per confronti)
    scheduled_date = models.DateField()
    # Data e ora effettiva in cui il ritiro è stato effettuato
    actual_pickup_datetime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default="scheduled")
    created_by = models.ForeignKey(
        User, related_name="pickups", null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ritiro di {self.cliente.ragionesociale} effettuato da {self.operatore.name} il {self.actual_pickup_datetime}"


class DailyItinerary(models.Model):
    operatore = models.ForeignKey(
        Operatore, on_delete=models.CASCADE, related_name="itineraries"
    )
    date = models.DateField()
    # I clienti selezionati per il ritiro in quella giornata.
    clienti = models.ManyToManyField(Cliente, related_name="itineraries")
    # Puoi aggiungere anche un campo per l'ordine dei punti se necessario.
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        related_name="itineraries",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        unique_together = ("operatore", "date")

    def __str__(self):
        return f"Itinerario {self.date} per {self.operatore}"
