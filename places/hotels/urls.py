from django.urls import path
from .views import HotelsView  # Import your view class

urlpatterns = [
    path('hotels/', HotelsView.as_view(), name='hotels-add'),  # Corrected path
]
