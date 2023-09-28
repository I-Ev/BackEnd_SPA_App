from rest_framework import serializers

from habits.models import Habit
from habits.validators import (AssociatedHabit_vs_RewardValidators, DurationValidators,
                               AsscoiatedHabitValidators, IsNiceValidators,
                               PeriodicityValidators)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [AssociatedHabit_vs_RewardValidators,
                      DurationValidators,
                      AsscoiatedHabitValidators,
                      IsNiceValidators,
                      PeriodicityValidators
        ]


class HabitPublicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['author', 'place', 'time', 'action', 'is_nice', 'periodicity', 'reward', 'duration']