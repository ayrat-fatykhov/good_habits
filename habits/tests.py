from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        """
        Cоздает тестового пользователя. Аутентифицирует пользователя
        """
        self.user = User.objects.create(email='test@sky.pro')
        self.user.set_password('123qwe567rty')
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """
        Тестирует создание привычки
        """
        response = self.client.post('/users/token/', {'email': 'test@sky.pro', 'password': '123qwe567rty'})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data_habit = {
            'creator': self.user.pk,
            'place': 'Test',
            'time': '00:00',
            'action': 'Test'
        }

        response = self.client.post(
            '/create/',
            data=data_habit
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                'id': 1,
                'creator': 1,
                'place': 'Test',
                'time': "00:00:00",
                'action': 'Test',
                'is_nice': False,
                'associated_habit': None,
                'periodicity': '1',
                'reward': None,
                'time_complete': '00:02:00',
                'is_public': False,
            }
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """
        Тестирует список привычек
        """
        self.maxDiff = None

        response = self.client.post('/users/token/', {'email': 'test@sky.pro', 'password': '123qwe567rty'})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        Habit.objects.create(
            creator=self.user,
            place='Test',
            time='0:00',
            action='Test'
        )

        response = self.client.get(
            '/list/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 3,
                        "place": "Test",
                        "time": "00:00:00",
                        "action": "Test",
                        "is_nice": True,
                        "periodicity": "1",
                        "reward": None,
                        "time_complete": "00:02:00",
                        "is_public": True,
                        "creator": 3,
                        "associated_habit": None
                     }
                            ]
            }
        )

    def test_view_habit(self):
        """
        Тестирует просмотр привычки
        """
        response = self.client.post('/users/token/', {'email': 'test@sky.pro', 'password': '123qwe567rty'})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            creator=self.user,
            place='Test',
            time='00:00',
            action='Test'
        )

        response = self.client.get(
            reverse('habits:habit_view', kwargs={'pk': habit.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': 5,
                'creator': 5,
                'place': 'Test',
                'time': "00:00:00",
                'action': 'Test',
                'is_nice': True,
                'associated_habit': None,
                'periodicity': '1',
                'reward': None,
                'time_complete': '00:02:00',
                'is_public': True,
            }
        )

    def test_update_habit(self):
        """
        Тестирует обновление привычки
        """

        response = self.client.post('/users/token/', {'email': 'test@sky.pro', 'password': '123qwe567rty'})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            creator=self.user,
            place='Test',
            time='00:00',
            action='Test'
        )

        data_habit_update = {
            'action': 'Test_1',
        }

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': habit.pk}),
            data=data_habit_update
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': 4,
                'creator': 4,
                'place': 'Test',
                'time': "00:00:00",
                'action': 'Test_1',
                'is_nice': True,
                'associated_habit': None,
                'periodicity': '1',
                'reward': None,
                'time_complete': '00:02:00',
                'is_public': True,
            }
        )

    def test_delete_habit(self):
        """
        Тестирует удаление привычки
        """
        response = self.client.post('/users/token/', {'email': 'test@sky.pro', 'password': '123qwe567rty'})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            creator=self.user,
            place='Test',
            time='00:00',
            action='Test'
        )

        response = self.client.delete(
            reverse('habits:habit_delete', kwargs={'pk': habit.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
