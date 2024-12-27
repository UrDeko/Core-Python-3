import requests
import statistics

api_key = "911e93f6fa0f726b571d7e30bf5ababe"

def weather_Moscow(api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat=55.7558&lon=37.6173&units=metric&appid={api_key}"
    request = requests.get(url)
    json = request.json()

    temperatures = []
    for weather_info in json.get("list"):
        temperatures.append(weather_info.get("main").get("temp"))
    avg_temp = round(statistics.mean(temperatures), 2)
    
    print(f"Average temperature for 5 days in Moscow: {avg_temp} degrees Celsius")

def weather_Berlin(api_key):
    city = "Berlin"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    request = requests.get(url)
    json = request.json()

    weather_description = json.get("weather")[0].get("main").lower()
    max_temp = json.get("main").get("temp_max")
    min_temp = json.get("main").get("temp_min")

    print(f"The weather in {city} is {weather_description}")
    print(f"Max temperature in {city}: {max_temp} degrees Celsius")
    print(f"Min temperature in {city}: {min_temp} degrees Celsius")

weather_Moscow(api_key)
weather_Berlin(api_key)