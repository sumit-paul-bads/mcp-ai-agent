from tool import get_weather

def agent_response(user_input):
    if "weather" in user_input.lower():
        try:
            city = user_input.lower().split("in")[-1].strip()
            data = get_weather(city)

            if "error" in data:
                return "Could not fetch weather."

            return f"Weather in {data['city']} is {data['temperature']}°C with {data['weather']}."
        except:
            return "Error processing request."

    return "I can help with weather info. Try asking: weather in Kolkata"