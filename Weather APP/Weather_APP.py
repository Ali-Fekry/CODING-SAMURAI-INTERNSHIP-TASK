import requests
import json

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # for Celsius
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌤 Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Condition: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")

    else:
        print("❌ City not found or API error. Please check the city name or your API key.\n")


def main():
    print("=== Weather App ===")
    api_key = "Your API key"  # Replace this with your actual OpenWeatherMap API key

    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye! 👋")
            break
        get_weather(city, api_key)

if __name__ == "__main__":
    main()
  
