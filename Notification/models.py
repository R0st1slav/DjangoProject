from django.db import models


class TypeDevice(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    type_device = models.ForeignKey(TypeDevice, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=15, decimal_places=6)
    longitude = models.DecimalField(max_digits=15, decimal_places=6)
    radius = models.IntegerField(default=0)

    def __str__(self):
        return self.name
