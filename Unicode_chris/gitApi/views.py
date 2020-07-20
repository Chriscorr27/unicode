from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from .form import UserForm

def userApi(request):
    if(request.method=='POST'):
        name = request.POST['username']
        url='https://api.github.com/users/{}'
        r = requests.get(url.format(name)).json()
        print(r)
        res = {
            'Login' : r['login'],
            'ID' : r['id'],
            'URL' : r['url'],
            "Followers_url" : r["followers_url"],
            'Name' : r['name'],
            'Email' : r['email'],
            'Public_repos' : r['public_repos']
        }
       # content ={'res' : r}
        return render(request,'ApiData.html',res)
    form = UserForm()
    content = {'form':form}
    return render(request,'userApi.html',content)

