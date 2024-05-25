from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from habits.tasks import send_message_to_bot
from users.permissions import IsCreator


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Отвечает за создание привычки
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Записывает создателя привычки"""
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        send_message_to_bot.delay(new_habit.id)
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """
    Выводит список привычек пользователя
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsCreator]

    def get_queryset(self):
        """
        Фильтрует вывод по пользователю
        """
        queryset = Habit.objects.filter(creator=self.request.user)
        return queryset


class HabitPublicListAPIView(generics.ListAPIView):
    """
    Выводит список публичных привычек
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Фильтрует привычки по признаку публичности
        """
        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за просмотр определеной привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Отвечает за изменение привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Отвечает за удаление привычки
    """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]
