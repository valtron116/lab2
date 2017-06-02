from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
from .models import Tasklist
from .serializers import TasklistSerializer
from rest_framework import viewsets
from .serializers import TagSerializer
from .models import Tag
from .models import Register
from .serializers import RegisterSerializer


class TaskDetailsView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TasklistCreateView(generics.ListCreateAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer


class TasklistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer


class TaskCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        list_id = self.kwargs.get('list_id', None)
        if list_id is not None:
            queryset = queryset.filter(tasklist_id = list_id)
        return queryset

    def perform_create(self, serializer):
        list_id = self.kwargs.get('list_id', None)
        try:
            tasklist = Tasklist.objects.get(pk=list_id)
        except Tasklist.DoesNotExist:
            raise NotFound()
        serializer.save(tasklist=tasklist)


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        list_id = self.kwargs.get('list_id', None)
        if list_id is not None:
            queryset = queryset.filter(tasklist_id = list_id)
        return queryset

class TagViewSet(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagTypeViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class RegisterView(generics.ListCreateAPIView):
	queryset = Register.objects.all()
	serializer_class = RegisterSerializer
