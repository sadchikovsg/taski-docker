"""Description."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Description."""

    class Meta:
        """Description."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
