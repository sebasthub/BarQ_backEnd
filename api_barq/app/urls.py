from django.urls import path
from app.views import produtos_list

urlpatterns = [
    path('', produtos_list)
]