from django.urls import path
from . import views

urlpatterns = [
    path('', views.visit_counter_view, name='visit_counter'),
]