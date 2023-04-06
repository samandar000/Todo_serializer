from .models import Todo
from rest_framework import serializers

class ToDoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    clas = serializers.CharField(max_length=100)
    task = serializers.CharField(max_length=100)
    description = serializers.CharField()
    completed = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        todo = Todo.objects.create(
            name = validated_data["name"],
            clas = validated_data["class"],
            task = validated_data["task"],
            description = validated_data["description"],
            completed = validated_data["completed"]

        )
        return todo
