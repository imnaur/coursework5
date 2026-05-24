from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsUserOrReadOnlyIfPublic

from .models import Habit
from .paginators import MyPagination
from .serializers import HabitSerializer, PublicHabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    pagination_class = MyPagination
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated, IsUserOrReadOnlyIfPublic]

        elif self.action in ["update", "partial_update", "retrieve"]:
            permission_classes = [IsAuthenticated, IsUserOrReadOnlyIfPublic]

        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsUserOrReadOnlyIfPublic]

        else:
            permission_classes = [IsAuthenticated, IsUserOrReadOnlyIfPublic]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Habit.objects.filter(public=True)
        my_habits = Habit.objects.filter(user=self.request.user)
        public_habits = Habit.objects.filter(public=True)
        return my_habits.union(public_habits)


class PublicHabit(ListAPIView):
    queryset = Habit.objects.filter(public=True)
    pagination_class = MyPagination
    serializer_class = PublicHabitSerializer
    permission_classes = [AllowAny,]