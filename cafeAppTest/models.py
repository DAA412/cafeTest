from django.core.exceptions import ValidationError
from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('в ожидании', 'В ожидании'),
        ('готово', 'Готово'),
        ('оплачено', 'Оплачено')
    ]

    table_number = models.IntegerField()
    items = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='в ожидании')

    def __str__(self):
        return f"Заказ {self.id} стола №{self.table_number}"

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

    def clean(self):
        if not isinstance(self.table_number, int):
            raise ValidationError('Номер стола должен быть целым числом')
        if self.table_number <= 0:
            raise ValidationError('Номер стола должен быть положительным')

    def calculate_total_price(self):
        items = self.items.split(',')
        total_price = 0
        for item in items:
            name, price = item.split(':')
            total_price += float(price)
        return total_price

