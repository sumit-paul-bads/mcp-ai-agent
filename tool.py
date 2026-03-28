import requests

API_KEY = "e2e4e1223577a62acddb4e86c2b4346d"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("main"):
        return {
            "city": city,
            "temperature": response["main"]["temp"],
            "weather": response["weather"][0]["description"]
        }
    else:
        return {"error": "City not found"}