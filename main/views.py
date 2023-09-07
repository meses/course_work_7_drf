from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import Habit
from main.pagination import MyPagination
from main.permissions import IsOwnerOrReadOnly, IsPublicOrReadOnly
from main.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]  # добавляем класс IsAuthenticated для проверки авторизации пользователя

    def perform_create(self, serializer):
        # Получаем авторизированного пользователя
        user = self.request.user
        # Передаем пользователя в качестве значения поля user в создаваемой привычке
        serializer.save(user=user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsPublicOrReadOnly]
    pagination_class = MyPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habit.objects.filter(Q(public=True) | Q(
                user=user))  # Q - это объект, который используется для создания сложных запросов в Django.
            # Он позволяет объединять несколько фильтров в одном запросе, используя операторы "или" и "и".
        else:
            return Habit.objects.filter(public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
