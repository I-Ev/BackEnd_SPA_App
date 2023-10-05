import os
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User
from utils.telegram import get_updates


# Create your tests here.
class HabitsTestCase(APITestCase):

    def create_user(self):
        """Создание пользователя"""
        self.user = User.objects.create(
            telegram_name='test_user',
            is_staff=False,
            is_active=True,
        )
        self.user.set_password('1234')
        self.user.save()

    def setUp(self) -> None:
        """Подготовка данных"""
        self.create_user()

        self.habit = Habit.objects.create(
            place='Test Place',
            time='12:00',
            action='Test Action',
            author=self.user
        )

    def test_list_habits(self):
        """Тестирование вывода списка привычек"""
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('habits:list-habit')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(
            len(response.json()) != 0
        )

    def test_create_lesson(self):
        """Тестирование создания привычки"""
        self.client.force_authenticate(self.user)

        data = {
            'place': 'Test Place 2',
            'time': '10:00',
            'action': 'Test Action 2'
        }

        response = self.client.post(
            reverse('habits:create-habit'),
            data=data

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED

        )


        self.assertEqual(
            Habit.objects.count(),
            2
        )

    def test_retrieve_habit(self):
        """Тестирование получения конкретной привычки"""
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('habits:view-habit', kwargs={'pk': self.habit.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Test Place')
        # Добавьте дополнительные проверки для других полей привычки

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        self.client.force_authenticate(self.user)

        data = {
            'place': 'Updated Place',
            'time': '12:00',
            'action': 'Updated Action'
        }

        response = self.client.patch(
            reverse('habits:update-habit', kwargs={'pk': self.habit.pk}),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, 'Updated Place')


    def test_delete_habit(self):
        """Тестирование удаления привычки"""
        self.client.force_authenticate(self.user)

        response = self.client.delete(
            reverse('habits:delete-habit', kwargs={'pk': self.habit.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(pk=self.habit.pk).exists())

class TelegramUtilsTestCase(TestCase):

    @patch('utils.telegram.requests.get')
    def test_get_updates(self, mock_get):

        #  фиктивные данные для mock-объекта
        mock_response = {"ok": True, "result": [{"update_id": 123, "message": {"chat": {"username": "test_user"}}}]}
        mock_get.return_value.json.return_value = mock_response

        updates = get_updates(0)

        # Проверяем, что функция возвращает ожидаемый результат
        self.assertEqual(updates, mock_response)

        # Проверяем, что запрос был выполнен с правильными аргументами
        token = os.getenv('TG_BOT_TOKEN')
        mock_get.assert_called_once_with(f'https://api.telegram.org/bot{token}/getUpdates?offset=1')
