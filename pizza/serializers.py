from rest_framework import serializers

from .models import Pizza, Topping


class ToppingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Topping
        fields = (
            'id',
            'name',
            'price',
            'pizza',
        )




class PizzaSerializer(serializers.ModelSerializer):
    
    topping_set = ToppingSerializer(many=True, read_only=True)
    total_pizza_price = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'topping_set',
            'total_price',
            'total_pizza_price',
        )
        read_only_fields = ('total_price',)

    def get_total_pizza_price(self, obj):
        total = obj.price
        toppings = obj.topping_set.all()        
        for topping in toppings:
            total += topping.price

        return total

