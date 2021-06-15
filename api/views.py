from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets,permissions


def home(req):
    return HttpResponse("HOME")


class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    permissions_classes=[permissions.AllowAny]

todo_list=TodoViewSet.as_view({
    'get':'list',
    'post':'create'
})

todo_delete=TodoViewSet.as_view({
    'delete':'destroy'
})