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


    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'topping_set',
        )





