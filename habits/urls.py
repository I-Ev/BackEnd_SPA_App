from django.urls import path

from habits.apps import HabitsConfig
from habits.views import PublicHabitsListAPIView, CreateHabitAPIView, RetrieveHabitAPIView, ListHabitAPIView, \
    UpdateHabitAPIView, DestroyHabitAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('public_habits/', PublicHabitsListAPIView.as_view(), name='public-habits'),

    path('my_habits/', ListHabitAPIView.as_view(), name='list-habit'),
    path('create/', CreateHabitAPIView.as_view(), name='create-habit'),
    path('retrieve/<int:pk>/', RetrieveHabitAPIView.as_view(), name='view-habit'),
    path('update/<int:pk>/', UpdateHabitAPIView.as_view(), name='update-habit'),
    path('delete/<int:pk>/', DestroyHabitAPIView.as_view(), name='delete-habit'),
]
