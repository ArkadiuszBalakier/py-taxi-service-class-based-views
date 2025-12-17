from django.urls import path

from .views import index, ManufacturerView, CarListView, DriverListView, CarDetailView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerView.as_view(), name="manufacturer-list"),
    path("car/", CarListView.as_view(), name="car-list"),
    path("driver/", DriverListView.as_view(), name="driver-list"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car"),
    path("driver/<int:pk>/", DriverDetailView.as_view(), name="driver"),
]

app_name = "taxi"
