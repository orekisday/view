from django.urls import path
from .views import CryptocurrencyListCreateView, WishlistListCreateView

urlpatterns = [
    path('cryptocurrencies/', CryptocurrencyListCreateView.as_view(), name='cryptocurrency-list-create'),
    path('wishlist/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
]
