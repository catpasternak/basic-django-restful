from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=17)
    color = models.CharField(verbose_name='Color', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = (
        (1, 'sedan'),
        (2, 'hatchback'),
        (3, 'pickup'),
        (4, 'coupe'),
    )
    type = models.IntegerField(verbose_name='Type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)