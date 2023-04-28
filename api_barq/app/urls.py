from django.urls import path
from app.views import produtos_list,produtos_get_by_id

urlpatterns = [
    path('', produtos_list),
    path('<int:pk>/', produtos_get_by_id)
]