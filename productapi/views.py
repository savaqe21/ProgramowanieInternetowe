from django.http import JsonResponse
from django.shortcuts import render

# Przykładowa lista produktów (może być zastąpiona modelem BD w rozszerzeniu)
DUMMY_PRODUCTS = [
    {"id": 101, "name": "Raspberry Pi 5 (8GB)", "price": 420.00, "in_stock": True},
    {"id": 102, "name": "Karta MicroSD 32GB (Klasa 10)", "price": 45.99, "in_stock": True},
    {"id": 103, "name": "Obudowa Argon ONE V2", "price": 139.90, "in_stock": True},
    {"id": 104, "name": "Zasilacz USB-C 5V/5A", "price": 55.00, "in_stock": False},
    {"id": 105, "name": "Moduł kamery Pi Camera v3", "price": 280.00, "in_stock": True},
    {"id": 106, "name": "Wyświetlacz dotykowy 5 cali", "price": 310.00, "in_stock": False},
]

# Endpoint API zwracający listę produktów w JSON
def product_list_api(request):
    """Zwraca listę produktów w formacie JSON."""
    return JsonResponse(DUMMY_PRODUCTS, safe=False)

# Widok dla strony frontendu (z przyciskiem)
def product_client_view(request):
    """Renderuje prosty frontend do komunikacji z API."""
    return render(request, 'productapi/index.html')