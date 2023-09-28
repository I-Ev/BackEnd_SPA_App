from rest_framework import serializers


class AssociatedHabit_vs_RewardValidators:
    """Валидатор исключает возможность указать по Привычке одновременно
     и Награду и Связанную привычку"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        assoc_habit = value.get('associated_habit')
        reward = value.get('reward')
        if assoc_habit and reward:
            raise serializers.ValidationError(
                'Нельзя указать одновременно связанную привычку и награду')

class DurationValidators:
    """Валидатор исключает возможность указать Продолжительность больше 120"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = value.get('duration')
        if duration > 120:
            raise serializers.ValidationError(
                'Время выполнения должно быть не больше 120 секунд')

class AsscoiatedHabitValidators:
    """Валидатор исключает попадание в связанные привычек без признака Приятная"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        assoc_habit = value.get('associated_habit')

        if not assoc_habit.is_nice:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки')

class IsNiceValidators:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_nice = value.get('is_nice')
        reward = value.get('reward')
        asscoiated_habit = value.get('associated_habit')

        if is_nice and (reward or asscoiated_habit):
            raise serializers.ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки')

class PeriodicityValidators:
    """Валидатор исключает возможность указать периодичность больше 7 дней"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = value.get('periodicity')
        if periodicity > 7:
            raise serializers.ValidationError(
                'Нельзя выполнять привычку реже, чем один раз в 7 дней.')