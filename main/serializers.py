from rest_framework import serializers
from main.models import Habit
from main.validators import validate_time_to_complete, validate_related_habit, validate_period
from users.models import User

class HabitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    time_to_complete = serializers.IntegerField(validators=[validate_time_to_complete])
    related_habit = serializers.PrimaryKeyRelatedField(queryset=Habit.objects.all(), required=False,
                                                       validators=[validate_related_habit])
    period = serializers.IntegerField(validators=[validate_period])

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        related_habit = data.get('related_habit')
        reward = data.get('reward')
        pleasant = data.get('pleasant')
        if related_habit and reward:
            raise serializers.ValidationError('Связанная привычка и вознаграждение не могут быть указаны одновременно')
        elif pleasant and (reward is not None or related_habit is not None):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки!")
        return data