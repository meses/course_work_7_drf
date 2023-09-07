from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Habit
from users.models import User
from django.urls import reverse


class HabitTestCase(APITestCase):

    def setUp(self):
        # Создание тестового пользователя
        self.user = User.objects.create_user(
            email='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)

        # Создание тестовой привычки
        self.habit = Habit.objects.create(
            user=self.user,
            place='Парк',
            time="13:00:00",
            action='Бег',
            pleasant=True,
            period=2,
            time_to_complete=115
        )

    def test_create_habit(self):
        """ Тест для создания привычек """
        url = reverse('main:habit-create')
        data = {
            'user': self.user.id,
            'place': 'Кофейня',
            'time': '09:00:00',
            'action': 'Читать новости',
            'pleasant': False,
            'period': 1,
            'time_to_complete': 15
        }

        response = self.client.post(url, data, format='json')  # Отправка POST-запроса для создания привычки

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)  # Проверка, что код статуса ответа равен 201 (Создан)
        self.assertEqual(Habit.objects.count(), 2)  # Проверка, что был создан объект привычки

    def test_list_habits(self):
        """ Тест для получения списка привычек """
        url = reverse('main:habit-list')  # Получение URL для получения списка привычек
        self.client.force_authenticate(user=self.user)  # Аутентификация пользователя
        response = self.client.get(url)  # Отправка GET-запроса на получение списка привычек
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа (должен быть 200 OK)
        self.assertEqual(len(response.data), 4)  # Проверка количества привычек в ответе (должно быть 4)

    def test_retrieve_habit(self):
        """ Тест для получения информации о конкретной привычке """
        url = reverse('main:habit-get', args=[self.habit.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Парк')  # Проверка места привычки

    def test_update_habit(self):
        """ Тест для обновления информации о привычке """
        url = reverse('main:habit-update',
                      args=[self.habit.id])  # Получаем URL для обновления привычки с определенным идентификатором
        data = {'place': 'Автобус'}  # Задаем новое значение для поля "place"
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)  # Отправляем PATCH-запрос на указанный URL с новыми данными
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'],
                         'Автобус')  # Проверяем, что значение поля "place" в ответе соответствует заданному значению

    def test_destroy_habit(self):
        """ Тест для удаления привычки """
        url = reverse('main:habit-delete', args=[self.habit.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(),
                         0)  # Проверяем, что количество объектов модели Habit равно 0,
        # что означает успешное удаление привычки.
