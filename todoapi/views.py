from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from .models import Task
import json

def todo_frontend_view(request):
    return render(request, 'todoapi/todo_frontend.html')

@csrf_exempt
def tasks_view(request):
    if request.method == "GET":
        data = list(Task.objects.values('id', 'title', 'done'))
        return JsonResponse({"tasks": data})

    if request.method == "POST":
        try:
            body = json.loads(request.body)
            title = body.get("title")

            if not title:
                return JsonResponse({"error": "Title is required"}, status=400)

            t = Task.objects.create(title=title)
            return JsonResponse({"id": t.id, "title": t.title, "done": t.done}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return HttpResponse(status=405)

@csrf_exempt
def task_done(request, task_id):
    if request.method == "PATCH":
        Task.objects.filter(id=task_id).update(done=True)
        return JsonResponse({"id": task_id, "done": True})

    return HttpResponse(status=405)

@csrf_exempt
def task_delete(request, task_id):
    if request.method == "DELETE":
        Task.objects.filter(id=task_id).delete()
        return HttpResponse(status=204)

    return HttpResponse(status=405)