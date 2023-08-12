from django.urls import path, include
from .views import DatasList

urlpatterns = [
    path('', DatasList.as_view() ),
]