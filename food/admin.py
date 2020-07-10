from django.contrib import admin
from . import models

@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Meal)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Customer)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Driver)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class RestaurantAdmin(admin.ModelAdmin):
    pass
