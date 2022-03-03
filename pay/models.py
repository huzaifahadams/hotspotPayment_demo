from django.db import models
from django.forms import CharField

# Create your models here.

class packages(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=2000)

    def __str__(self):
        return self.name
        
class payment_num(models.Model):
    phone_num = models.BigIntegerField()

    def __str__(self):
        return self.phone_num


class info(models.Model):
    title = models.CharField(max_length=500)
    #logo = models.ImageField()

    def __str__(self):
        return self.title