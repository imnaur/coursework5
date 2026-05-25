from rest_framework import serializers

from .models import Habit
from .validators import (
    validate_execution_time,
    validate_habit,
    validate_only_one_compensation,
    validate_regularity,
    validate_related_is_pleasant
)


def run_all_validators(self, attrs):
    validate_only_one_compensation(attrs, self)
    validate_execution_time(attrs, self)
    validate_related_is_pleasant(attrs, self)
    validate_habit(attrs, self)
    validate_regularity(attrs, self)
    return attrs

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        return run_all_validators(self, attrs)


class PublicHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('user', 'location', 'time', 'action', 'regularity', 'time_required')

class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        return run_all_validators(self, attrs)