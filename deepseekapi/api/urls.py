from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.GenerateView.as_view(), name='generate'),
]