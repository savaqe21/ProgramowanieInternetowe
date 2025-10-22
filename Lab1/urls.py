from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('witaj/', include('witaj.urls')),
    path('', include('frontend_demo.urls')),
]
