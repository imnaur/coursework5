from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.permissions import IsUserOrReadOnlyIfPublic
from .paginators import MyPagination
from .models import Habit
from .serializers import HabitSerializer, PublicHabitSerializer, HabitCreateSerializer


class UserHabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    pagination_class = MyPagination
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(public=True)
    pagination_class = MyPagination
    serializer_class = PublicHabitSerializer
    permission_classes = [AllowAny]


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnlyIfPublic]
