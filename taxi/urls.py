from django.urls import path

from .views import index, ManufacturerView, CarListView, DriverListView, CarDetailView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerView.as_view(), name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="cars"),
    path("drivers/", DriverListView.as_view(), name="drivers"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car"),
    path("driver/<int:pk>/", DriverDetailView.as_view(), name="driver"),
]

app_name = "taxi"
