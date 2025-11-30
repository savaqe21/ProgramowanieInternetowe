from django.db import models

class Visit(models.Model):
    """Model do przechowywania licznika odwiedzin strony (Django)."""
    # Pole przechowujące liczbę całkowitą, domyślnie 0
    count = models.IntegerField(default=0) 

    def __str__(self):
        return f"Odwiedziny: {self.count}"