from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
        ]


class HabitPublicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['author', 'place', 'time', 'action', 'is_nice', 'periodicity', 'reward', 'duration']