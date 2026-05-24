from rest_framework.routers import SimpleRouter
from django.urls import path, include
from habit_tracker.apps import HabitTrackerConfig
from .views import HabitViewSet
from .views import PublicHabit

app_name = HabitTrackerConfig.name
router = SimpleRouter()
router.register(r"habit", HabitViewSet, basename='habit')

urlpatterns = [
    path('', include(router.urls)),
    path('public/', PublicHabit.as_view(), name='public')
]