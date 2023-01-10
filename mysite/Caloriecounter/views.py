from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from Caloriecounter.models import Person
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from Caloriecounter.serializers import UserSerializer, GroupSerializer, PersonSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class Personlist(APIView):
    def get(self,request,format=None):
            person = Person.objects.all().order_by('first_name')
            serializer =PersonSerializer(person,many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
            data=JSONParser().parse(request)
            serializer = PersonSerializer (data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class persondetail(APIView):
    def get_object(self,pk):
        try : 
            print(Person.objects.get(pk=pk))
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST
        
    def get(self,request,pk,format=None):
        person=self.get_object(pk)
        serializer=PersonSerializer(person)
        return Response(serializer.data)
    
    def put (self,request,pk,format=None):
        person=self.get_object(pk)
        serializer=PersonSerializer(Person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        person=self.get_object(pk)
        Person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def hey(request):
    data="hey"
    return HttpResponse(data)

def home(request):
    context = {'name':'Manusharma'}
    return render(request,'home.html',context)










# Create your views here.
