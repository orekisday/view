from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cryptocurrency, Wishlist
from .serializers import CryptocurrencySerializer, WishlistSerializer

class CryptocurrencyListCreateView(generics.ListCreateAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

class WishlistListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
