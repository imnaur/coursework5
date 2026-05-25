from django.urls import path

from .apps import HabitTrackerConfig
from .views import UserHabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, HabitDetailUpdateDestroyAPIView

app_name=HabitTrackerConfig.name

urlpatterns = [
    path('', UserHabitListAPIView.as_view(), name='user-habits'),
    path('public/', PublicHabitListAPIView.as_view(), name='public-habits'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('<int:pk>/', HabitDetailUpdateDestroyAPIView.as_view(), name='habit-detail'),
]
