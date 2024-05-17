from rest_framework import serializers
from .models import Cryptocurrency, Wishlist

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['id', 'name', 'price']

class WishlistSerializer(serializers.ModelSerializer):
    cryptocurrencies = CryptocurrencySerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'cryptocurrencies']
