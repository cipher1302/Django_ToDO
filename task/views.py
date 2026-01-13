from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.
class TaskApiView(APIView):
    
    def get(self,request):
        tasks = Task.objects.all()
        return Response({'tasks':TaskSerializer(tasks,many=True).data})
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        new_task = Task.objects.create(
            title = request.data['title']
        )
        return Response({
            'message':"Task created successfully",
            'new_task': TaskSerializer(new_task).data
        })