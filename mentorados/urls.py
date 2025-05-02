from django.urls import path
from .views import mentorados

urlpatterns = [
    path('', mentorados.as_view(), name='mentorados'),
]
