from django.db import models


class PC(models.Model):
    price = models.TextField(blank=True, null=True)
    gpu = models.TextField(blank=True, null=True)
    cpu = models.TextField(blank=True, null=True)
    ram = models.TextField(blank=True, null=True)
    power_supply = models.TextField(blank=True, null=True)
    memory = models.TextField(blank=True, null=True)
    cooler = models.TextField(blank=True, null=True)
    case = models.TextField(blank=True, null=True)
    motherboard = models.TextField(blank=True, null=True)

    gpu_market = models.CharField(max_length=100, blank=True, null=True)
    cpu_market = models.CharField(max_length=100, blank=True, null=True)
    ram_market = models.CharField(max_length=100, blank=True, null=True)
    power_supply_market = models.CharField(max_length=100, blank=True, null=True)
    memory_market = models.CharField(max_length=100, blank=True, null=True)
    cooler_market = models.CharField(max_length=100, blank=True, null=True)
    case_market = models.CharField(max_length=100, blank=True, null=True)
    motherboard_market = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Конфигурация ПК #{self.id}"