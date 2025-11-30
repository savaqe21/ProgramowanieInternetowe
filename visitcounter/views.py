from django.shortcuts import render
from .models import Visit

def visit_counter_view(request):
    """
    Widok, który zwiększa licznik odwiedzin strony w bazie danych.
    """
    # Pobiera rekord Visit lub tworzy go, jeśli nie istnieje
    try:
        visit_obj = Visit.objects.get(pk=1) 
    except Visit.DoesNotExist:
        # Tworzy nowy rekord, jeśli to pierwsze uruchomienie
        visit_obj = Visit.objects.create(pk=1, count=0)

    # Zwiększa licznik odwiedzin
    visit_obj.count += 1
    visit_obj.save()

    # Przekazuje wartość licznika
    context = {
        'visit_count': visit_obj.count
    }

    # 4. Renderuje szablon
    return render(request, 'visitcounter/visit_counter.html', context)