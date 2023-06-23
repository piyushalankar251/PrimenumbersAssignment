from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    items = models.JSONField()
    lat_long = models.CharField(max_length=100)
    full_details = models.JSONField()

    def __str__(self):
        return self.name
