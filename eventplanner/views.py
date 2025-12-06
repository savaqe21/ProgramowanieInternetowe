from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event, Comment
from .forms import EventForm, CommentForm
from django.views.decorators.csrf import csrf_exempt

# --- WIDOKI FRONTENDOWE ---

def event_dashboard_view(request):
    """ Renderuje główny pulpit wydarzeń. """

    # Pobieramy wydarzenia i komentarze
    events = Event.objects.filter(is_active=True).order_by('-date').prefetch_related('comments')

    context = {
        'events': events,
        'CommentForm': CommentForm(),
    }
    return render(request, 'eventplanner/event_dashboard.html', context)

def create_event_view(request):
    """ Obsługuje formularz tworzenia wydarzenia (GET i POST). """

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_dashboard')
    else:
        form = EventForm()

    context = {
        'form': form,
        'title': 'Utwórz nowe wydarzenie'
    }
    return render(request, 'eventplanner/create_event.html', context)

def add_comment_view(request, event_id):
    """ Obsługuje dodawanie komentarza do konkretnego wydarzenia (POST). """

    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'event': event.id})

        if form.is_valid():
            form.save()
            return redirect('event_dashboard')

    return redirect('event_dashboard')

# --- WIDOK API (GŁOSOWANIE BEZPOŚREDNIO NA EVENT) ---

@csrf_exempt
def event_vote_api(request, event_id):
    """ API Endpoint: Zwiększa licznik głosów dla danego wydarzenia (POST/AJAX). """

    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)

        event.votes += 1
        event.save()

        return JsonResponse({'status': 'success', 'new_votes': event.votes}, status=200)

    return HttpResponse(status=405)

@csrf_exempt
def event_delete_api(request, event_id):
    """ API Endpoint: Usuwa wydarzenie o podanym ID. """

    if request.method == 'DELETE':
        # Sprawdzamy, czy wydarzenie istnieje i je pobieramy
        event = get_object_or_404(Event, pk=event_id)

        # Usuwamy wydarzenie
        event.delete()

        # Zwracamy status 204 No Content (standard REST dla usunięcia)
        return HttpResponse(status=204)

    return HttpResponse(status=405) # Method Not Allowed