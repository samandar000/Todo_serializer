from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Todo
from .serializers import ToDoSerializer


class TodoView(APIView):
    def get(self, request: Request) -> Response:
        todos = Todo.objects.all()
        print(type(todos[0]))
      
        
        serilazer = ToDoSerializer(todos, many=True)
        data = {
            "results": serilazer.data
        }
      


        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
