from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    if request.method == "POST":
        city_name = request.POST["cityName"]
        api_key = "dcd522e54ae503a15e03a90b655d3828"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        weather_data = {
            "name": data["name"],
            "country": data["sys"]["country"],
            "temp": int(data["main"]["temp"]) - 273,
            "weather": data["weather"][0]["main"]
        }
        return render(request, "home.html", {"weather_data": weather_data})
    else:
        return render(request, "home.html")