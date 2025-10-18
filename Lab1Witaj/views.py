from django.http import HttpResponse

# Create your views here.
def hello(request):
  return HttpResponse('Witaj w Django!')