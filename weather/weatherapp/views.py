from django.shortcuts import render
import requests#pip install requests
from django.contrib import messages

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='kathmandu'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978'
    param={ 'units':'metric'}
    
    data=requests.get(url,param).json()
    try:
        desc=data['weather'][0]['description']#to fetch the discription from the json data 
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']#to fetch the tempetaure fron the json data
        wind=data['wind']['speed']
        humidity=data['main']['humidity']
        context={
            'temp':temp,
            'city':city,
            'desc':desc,
            'icon':icon,
            'wind':wind,
            'humidity':humidity
        }
        return render(request,'index.html',context)
    except:
        temp=0
        desc='no data found'
        messages.error(request,'city is not found')
        return render(request,'index.html',{'temp':temp,'desc':desc})

   