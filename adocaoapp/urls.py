from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/adoptions/', include('apps.adoptions.urls')),  # ajuste conforme seu app
]