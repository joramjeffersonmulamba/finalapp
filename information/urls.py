from django.urls import path
from . import views  # Import app views

urlpatterns = [
    path('vip/', views.vip, name='vip'),  # Map URL to the view function
    path('howtoplay/', views.howtoplay, name='howtoplay'),
]
