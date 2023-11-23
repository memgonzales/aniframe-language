from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeSerializer
from .models import Codes

# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def code(request):

    if request.method == 'GET':
        code = Codes.objects.all()
        serializer = CodeSerializer(code, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def code_detail(request, pk):
    try:
        code = Codes.objects.get(pk=pk)
    except Codes.Doescodexist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
