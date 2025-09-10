from django.db import models



class PC(models.Model):
    # Существующие поля (оставляем как есть)
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

    gpu_link = models.TextField(blank=True, null=True)
    cpu_link = models.TextField(blank=True, null=True)
    ram_link = models.TextField(blank=True, null=True)
    power_supply_link = models.TextField(blank=True, null=True)
    memory_link = models.TextField(blank=True, null=True)
    cooler_link = models.TextField(blank=True, null=True)
    case_link = models.TextField(blank=True, null=True)
    motherboard_link = models.TextField(blank=True, null=True)

    # Исправленные поля (добавлены обязательные параметры)
    COMPONENT_TYPES = [
        ('RAM', 'Оперативная память'),
        ('CPU', 'Процессор'),
        ('GPU', 'Видеокарта'),
        ('COOLER', 'Кулер процессора'),
        ('MB', 'Материнская плата'),
        ('CASE_COOLER', 'Корпусное охлаждение'),
    ]

    component_type = models.CharField(
        max_length=20,  # Добавлен max_length
        choices=COMPONENT_TYPES,
        blank=True,  # Добавлено по аналогии с другими полями
        null=True
    )

    name = models.CharField(
        max_length=255,  # Обязательный параметр для CharField
        blank=True,
        null=True
    )

    price_component = models.DecimalField(
        max_digits=10,  # Обязательный параметр - общее количество цифр
        decimal_places=2,  # Количество цифр после запятой
        blank=True,
        null=True
    )

    url = models.URLField(
        blank=True,  # Добавлено для consistency
        null=True
    )

    def __str__(self):
        return f"Конфигурация ПК #{self.id}"
