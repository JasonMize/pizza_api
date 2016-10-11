from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length = 50, blank=True, null=True)
    price = models.IntegerField()


class Topping(models.Model):
    name = models.CharField(max_length = 50, blank=True, null=True)
    pizza = models.ForeignKey('Pizza')
    price = models.IntegerField()




