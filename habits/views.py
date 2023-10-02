from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from habits.models import Habit
from habits.paginators import MyHabitPaginator
from habits.permissions import IsAuthor, ReadOnly
from habits.serializers import HabitSerializer, HabitPublicListSerializer

class CreateHabitAPIView(generics.CreateAPIView):
    """Создает новую привычку"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.author = get_object_or_404(User, id=self.request.user.id)
        habit.save()

class RetrieveHabitAPIView(generics.RetrieveAPIView):
    """Получает привычку по ID"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthor, IsAuthenticated]
    lookup_field = 'id'

class UpdateHabitAPIView(generics.UpdateAPIView):
    """Обновляет привычку по ID"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthor, IsAuthenticated]
    lookup_field = 'id'

class DestroyHabitAPIView(generics.DestroyAPIView):
    """Удаляет привычку по ID"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthor, IsAuthenticated]
    lookup_field = 'id'

class ListHabitAPIView(generics.ListAPIView):
    """Получает список привычек пользователя"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthor, IsAuthenticated]
    pagination_class = MyHabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(author=get_object_or_404(User, id=self.request.user.id))

class PublicHabitsListAPIView(generics.ListAPIView):
    """Получает список публичных привычек"""
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitPublicListSerializer
    permission_classes = [ReadOnly]
