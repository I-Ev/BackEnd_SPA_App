from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import MyHabitPaginator
from habits.permissions import IsAuthor, ReadOnly
from habits.serializers import HabitSerializer, HabitPublicListSerializer


# Create your views here.
class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def list(self, request, *args, **kwargs):
        self.pagination_class = MyHabitPaginator()
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        #
        # new_habit = serializer.save()
        # print(f"DEBUG: User before setting author: {new_habit.author}")
        # new_habit.author = self.request.user
        # print(f"DEBUG: User after setting author: {new_habit.author}")
        # new_habit.save()

        # """Вью сет для модели привычки"""
        # queryset = Habit.objects.all()
        # serializer_class = HabitSerializer
        #
        # def perform_create(self, serializer):
        #     new_habit = serializer.save()
        #     new_habit.author = self.request.user
        #     new_habit.save()
        #
        #     # serializer.validated_data['author'] = self.request.user
        #     # serializer.save()



class PublicHabitsListAPIView(generics.ListAPIView):
    """Получает список публичных привычек"""
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitPublicListSerializer
    permission_classes = [ReadOnly]
