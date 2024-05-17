from django.contrib.auth.models import User
from django.db import models

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrencies = models.ManyToManyField(Cryptocurrency)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
