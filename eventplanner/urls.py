from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_dashboard_view, name='event_dashboard'),
    path('create/', views.create_event_view, name='create_event'),

    # Obsługa POST formularza komentarzy
    path('comment/add/<int:event_id>/', views.add_comment_view, name='add_comment'),

    # API dla głosowania na Wydarzenie
    path('api/events/<int:event_id>/vote/', views.event_vote_api, name='event_vote_api'),

  # Usuwanie Wydarzenia
    path('api/events/<int:event_id>/delete/', views.event_delete_api, name='event_delete_api'),
]