from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
@api_view(['GET','PUT','POST','PATCH','DELETE'])
def index(request,id=None):
    if request.method=="GET":
        # id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=="POST":
        print(request.data)
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response("Kuch to gadbad hai Bhaisahab",status=status.HTTP_400_BAD_REQUEST)

    if request.method=="PUT":
        print(request.data)
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        print(stu)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("Kuch to gadbad hai updation me ",status=status.HTTP_400_BAD_REQUEST)
    if request.method=="PATCH":
        print("CHala")
        print(request.data)
        id =request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
    if request.method=="DELETE":
       print(request.data)
       # id=request.data.get('id')
       print(id)
       if id is not None:
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response("Data Deleted",status=status.HTTP_200_OK)
       else :
           return Response("You have not selected any id")