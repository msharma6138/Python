from django.shortcuts import render
from django.http import HttpResponse

def hey(request):
    data="hey"
    return HttpResponse(data)

def home(request):
    context = {'name':'Manusharma'}
    return render(request,'home.html',context)
# Create your views here.
