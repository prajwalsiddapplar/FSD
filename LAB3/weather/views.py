
import requests
from django.shortcuts import render

def home(request):
    data = {}
    error = ""

    if request.method == "POST":
        city = request.POST.get("city")
        api_key = "YOUR_API_KEY"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        result = response.json()

        if result.get("cod") == 200:
            data = {
                "city": result["name"],
                "temperature": result["main"]["temp"],
                "description": result["weather"][0]["description"]
            }
        else:
            error = "Invalid city name"

    return render(request, "home.html", {"data": data, "error": error})

