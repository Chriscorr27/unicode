from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import InputForm
from .task1 import task as t
# Create your views here.

def task2(request,a,b):
    res=t(a,b)
    return JsonResponse(res)

def task1(request):
    if(request.method=='POST'):
        a = int(request.POST['starting'])
        b = int(request.POST['ending'])
        res = t(a,b)
        return JsonResponse(res)
    form = InputForm()
    content = {'form' : form}
    return render(request,'taskInput.html',content)

def home(request):
    
    return render(request,'home.html')
