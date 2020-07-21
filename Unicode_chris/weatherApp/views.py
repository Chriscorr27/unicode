from django.shortcuts import render
from django.http import JsonResponse
from .forms import InputForm
import requests
# Create your views here.
def search(request):
    form = InputForm()
    count_1 = False
    if request.method == 'POST':
        city = request.POST['city']
        url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6348833852f0c879ca857e9b93980f4a'
        r=requests.get(url.format(city)).json()
        weather_info={
            'city': city ,
            'temp': r['main']['temp'] ,
            'desc': r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }
        count_1=True
    else:
        weather_info={}
    
    
    
    content = {'form':form,'weather':weather_info,'count_1':count_1}
    return render(request,'WeatherHome.html',content)