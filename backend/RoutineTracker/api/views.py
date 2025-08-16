from django.shortcuts import render
from django.http import HttpResponse

from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.
def toDoListView(request) :
    return HttpResponse('To do list view')

@method_decorator(csrf_exempt, name='dispatch')
class CsrfExemptTokenView(TokenObtainPairView):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_todos(request):
    todos = ToDo.objects.filter(user=request.user).order_by('-created_at')
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)