from django.shortcuts import render
from django.http import JsonResponse
from .forms import InputForm
import requests
from .models import City_weather
# Create your views here.
def search(request):
    form = InputForm()
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6348833852f0c879ca857e9b93980f4a'
    weathers = []
    err_msg=''
    search = False
    if request.method == 'POST':
        city = request.POST['city']
        r=requests.get(url.format(city)).json()
        if r['cod']==200:
            #isCityInDataBase = City_weather.objects.filter(city=city).exists()
            city_obj =City_weather.objects.get_or_create(name=city)
            city_obj[0].count+=1
            print(city_obj[0].count)
            city_obj[0].save()
            
            weather_info={
                'city': city ,
                'temp': r['main']['temp'] ,
                'desc': r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'count' : city_obj[0].count
            }
            search = True
            weathers.append(weather_info)
            content = {'form':form,'weathers':weathers,'search':search,'err_msg':err_msg}
            return render(request,'WeatherHome.html',content)
        else:
            err_msg=city+' doesnot exist'
            print(err_msg)
        
            
   
    cities=City_weather.objects.order_by('-count')
    city_count = City_weather.objects.all().count()
    if(city_count>3):
        city_count=3
    for i in range(city_count):
        city = cities[i]
        r=requests.get(url.format(city.name)).json()
        weather_info={
                'city': city.name ,
                'temp': r['main']['temp'] ,
                'desc': r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'count' : city.count
            }
        weathers.append(weather_info)

        

    
    content = {'form':form,'weathers':weathers,'search':search,'err_msg':err_msg}
    return render(request,'WeatherHome.html',content)