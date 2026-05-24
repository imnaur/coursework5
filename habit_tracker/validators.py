from datetime import timedelta

from pycodestyle import continued_indentation
from rest_framework.serializers import ValidationError


def validate_only_one_compensation(attrs, serializer):
    """Функция проверяет, что заполнено только одно поле: связанная привычка ИЛИ вознаграждение"""
    related_habit = attrs.get("related_habit")
    compensation = attrs.get("compensation")

    if serializer.instance:
        if not "related_habit" in attrs:
            related_habit = serializer.instance.related_habit
        if not "compensation" in attrs:
            compensation = serializer.instance.compensation
    if related_habit and compensation:
        raise ValidationError(
            "Нельзя выбирать одновременно приятную привычку и вознаграждение!"
        )


def validate_execution_time(attrs, serializer):
    """Функция проверяет продолжительность привычки (не более 2 минут)"""
    time_required = attrs.get("time_required")

    if serializer.instance:
        if not "time_required" in attrs:
            time_required = serializer.instance.time_required
    if time_required:
        if time_required > timedelta(seconds=120):
            raise ValidationError("Привычка не должна длиться более 2 минут!")


def validate_related_is_pleasant(attrs, serializer):
    """Функция проверяет, что в связанные привычки попадают только привычки с признаком приятности"""
    related_habit = attrs.get("related_habit")

    if serializer.instance and "related_habit" not in attrs:
        related_habit = serializer.instance.related_habit

        if related_habit:
            if not related_habit.is_pleasant:
                raise ValidationError(
                    "В связанные привычки попадают только привычки с приятным признаком!"
                )


def validate_habit(attrs, serializer):
    """Функция проверяет, нет ли у приятной привычки вознаграждения или связи"""
    is_pleasant = attrs.get("is_pleasant")
    related_habit = attrs.get("related_habit")
    compensation = attrs.get("compensation")

    if serializer.instance and "is_pleasant" not in attrs:
        is_pleasant = serializer.instance.is_pleasant
    if serializer.instance and "related_habit" not in attrs:
        related_habit = serializer.instance.related_habit
    if serializer.instance and "compensation" not in attrs:
        compensation = serializer.instance.compensation

        if is_pleasant:
            if related_habit:
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки!"
                )
            if compensation:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения!"
                )


def validate_regularity(attrs, serializer):
    """Функция проверяет регулярность выполнения привычки (не реже 1 раза в неделю)"""
    regularity = attrs.get("regularity")
    regular_habit = 1

    if serializer.instance and "regularity" not in attrs:
        regularity = serializer.instance.regularity

    if regularity is not None:
        if regularity < 1:
            raise ValidationError(
                "Периодичность выполнения должна быть не меньше 1 дня!"
            )

        if regularity > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней (раз в неделю)!"
            )
