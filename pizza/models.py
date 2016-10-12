from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length = 50, blank=True, null=True)
    price = models.IntegerField()

    def total_price (self):
        total = self.price
        toppings = self.topping_set.all()        
        for topping in toppings:
            total += topping.price

        return total



class Topping(models.Model):
    name = models.CharField(max_length = 50, blank=True, null=True)
    pizza = models.ForeignKey('Pizza')
    price = models.IntegerField()




