from django.shortcuts import render
from rest_framework import viewsets
from .serielizers import TodoSerializer
from .models import Todo


# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
