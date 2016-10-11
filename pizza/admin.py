from django.contrib import admin

from .models import Pizza, Topping


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'pizza', 'price',)

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)    
