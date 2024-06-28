from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer
from datetime import date

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def due_today(self, request):
        tasks = Task.objects.filter(due_date=date.today())
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
