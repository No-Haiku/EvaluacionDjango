from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=255)
    units_sold = models.PositiveIntegerField()

    def __str__(self):
        return self.nickname

class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    permalink = models.URLField()

    def __str__(self):
        return self.title
