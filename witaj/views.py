from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def hello(request):
    """Podstawowy widok powitalny"""
    return HttpResponse("Witaj w Django!")


def hello_name(request, name):
    """Dynamiczny widok powitalny z parametrem name"""
    return HttpResponse(f"Witaj, {name}!")


def hello_template(request, name):
    """Widok powitalny używający szablonu HTML"""
    return render(request, "witaj/hello.html", {"name": name})


def current_time(request):
    """Widok wyświetlający aktualną datę i godzinę - ZADANIE DOMOWE"""
    now = datetime.now()
    # Format: Dzisiaj jest: 22.09.2025, godzina: 18:42
    formatted_date = now.strftime("%d.%m.%Y")
    formatted_time = now.strftime("%H:%M")

    context = {
        'date': formatted_date,
        'time': formatted_time
    }

    return render(request, "witaj/time.html", context)
