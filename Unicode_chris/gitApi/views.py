from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from .form import UserForm

def userApi(request):
    if(request.method=='POST'):
        name = request.POST['username']
        url='https://api.github.com/users/{}'
        r = requests.get(url.format(name)).json()
        #print(r)
        return JsonResponse(r)
    form = UserForm()
    content = {'form':form}
    return render(request,'userApi.html',content)

