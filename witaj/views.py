from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return HttpResponse("Witaj na stronie głównej!<br>Przejdź do /hello/ lub /time/")

def hello(request):
    return HttpResponse("Witaj w Django!")

def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})

def current_time(request):
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.%Y")
    formatted_time = now.strftime("%H:%M")
    context = {'date': formatted_date, 'time': formatted_time}
    return render(request, "witaj/time.html", context)
