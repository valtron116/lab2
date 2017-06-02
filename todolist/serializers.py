from rest_framework import serializers
from .models import Task, Tasklist
from rest_framework import generics
from .models import Tag
from .models import Register


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'completed', 'date_created', 'date_modified', 'due_date', 'priority')
        read_only_fields = ('date_created', 'date_modified')


class TasklistSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tasklist
        fields = ('name', 'tasks')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')

class RegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = Register
		fields = ('first_name', 'last_name', 'email', 'password')