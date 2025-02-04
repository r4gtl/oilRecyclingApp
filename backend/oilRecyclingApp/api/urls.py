from django.urls import path
from .views import (
    ClienteListCreateAPIView,
    ZonaListCreateAPIView,
    OperatoreListCreateAPIView,
    ZoneRetrieveUpdateDestroyAPIView,
    ClienteRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("clienti/", ClienteListCreateAPIView.as_view(), name="cliente-list-create"),
    path("zone/", ZonaListCreateAPIView.as_view(), name="zona-list-create"),
    path(
        "operatori/", OperatoreListCreateAPIView.as_view(), name="operatore-list-create"
    ),
    path(
        "zone/<int:pk>/",
        ZoneRetrieveUpdateDestroyAPIView.as_view(),
        name="zona-detail-update-delete",
    ),
    path(
        "cliente/<int:pk>/",
        ClienteRetrieveUpdateDestroyAPIView.as_view(),
        name="cliente-detail-update-delete",
    ),
]
