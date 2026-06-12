from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Habit
from users.models import CustomUser
from django.urls import reverse

User = get_user_model()


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='german@mail.ru', password='123abc', chat_id='112858473',
                                                   username='testing')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            action='Выпить стакан воды с лимоном',
            location='Дома',
            time='08:00:00',
            public=True,
            time_required="00:01:30",
            regularity=1,
            is_pleasant=False,
        )

    def test_get_habits_list(self):
        """Тест получения списка привычек пользователя"""
        url = reverse("habit_tracker:user-habits")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(
            Habit.objects.count(), 1
        )
        self.assertEqual(data["results"][0]["action"], self.habit.action)

    def test_get_public_habit(self):
        """Тест получения публично опубликованных привычек"""
        url = reverse("habit_tracker:public-habits")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habit_create(self):
        """Тест создания одной привычки"""
        url = reverse("habit_tracker:habit-create")
        data = {
            "user": self.user.pk,
            "action": "Прогулка после ужина",
            "location": "Двор",
            "time": "20:00:00",
            "public": True,
            "time_required": "00:01:30",
            "regularity": 1,
            "is_pleasant": False
        }
        response = self.client.post(url, data)
        if response.status_code != 201:
            print("\n❌ Ошибка создания:", response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_update(self):
        """Тест обновления одной привычки"""
        url = reverse("habit_tracker:habit-detail", args=(self.habit.pk,))
        data = {
            "action": "Бег по утрам",
            "location": "Стадион",
            "time": '08:00:00',
            "public": True,
            "time_required": "00:01:30",
            "regularity": "1",
            "is_pleasant": False}

        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(response.json().get("action"), "Бег по утрам")
        self.assertEqual(response.json().get("location"), "Стадион")

    def test_habit_delete(self):
        """Тест удаления одной привычки"""
        url = reverse("habit_tracker:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Habit.objects.count(), 0)


class CustomUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@mail.ru',
            password='password123',
            phone_number='+4915116758899',
            chat_id='1177277449',
            username='testing'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_users_list(self):
        """Тест на получения списка пользователей"""
        url = reverse("users:users-list")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
