from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q


class Zona(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name="zone", null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class ClienteManager(models.Manager):
    def ritiri_del_giorno(self):
        oggi = timezone.localdate()
        # Se oggi è compreso tra (pickup_date - tolerance_before) e (pickup_date + tolerance_after)
        return self.filter(
            Q(pickup_date__gte=oggi - models.F("tolerance_before"))
            & Q(pickup_date__lte=oggi + models.F("tolerance_after"))
        )


class Cliente(models.Model):
    pickup_date = models.DateField()
    tolerance_before = models.IntegerField(
        default=0, help_text="Giorni di tolleranza prima della data prevista"
    )
    tolerance_after = models.IntegerField(
        default=0, help_text="Giorni di tolleranza dopo la data prevista"
    )
    zone = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="clienti")
    # Campo per registrare l'orario dell'ultimo ritiro effettuato
    last_pickup_datetime = models.DateTimeField(null=True, blank=True)
    ragionesociale = models.CharField(max_length=50, blank=False, null=False)
    indirizzo = models.CharField(max_length=100, blank=True, null=True)
    cap = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    sito_web = models.CharField(max_length=200, blank=True, null=True)
    e_mail = models.EmailField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name="clienti", null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    objects = ClienteManager()

    def __str__(self):
        return self.name


class Operatore(models.Model):
    name = models.CharField(max_length=100)
    # Relazione ManyToMany con Zone, tramite il modello intermedio Assignment
    zone = models.ManyToManyField(Zona, through="Assignment", related_name="operatori")
    created_by = models.ForeignKey(
        User, related_name="operatori", null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    operatore = models.ForeignKey(
        Operatore, on_delete=models.CASCADE, related_name="assignments"
    )
    zone = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="assignments")
    # La data in cui il camionista è assegnato a questa zona
    date = models.DateField()
    created_by = models.ForeignKey(
        User,
        related_name="assignments",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = ("operatore", "zone", "date")
        ordering = ["date"]

    def __str__(self):
        return f"{self.operatore.name} - {self.zone.name} il {self.date}"
