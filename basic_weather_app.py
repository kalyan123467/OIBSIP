# Basic Weather App using OpenWeatherMap API
import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n===== WEATHER REPORT =====")
            print(f"City        : {data['name']}")
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Humidity    : {data['main']['humidity']}%")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")
            print("==========================")

        elif response.status_code == 404:
            print("Error: Invalid city name.")
        else:
            print("Unable to fetch weather data.")

    except Exception as error:
        print("Error:", error)

def main():
    while True:
        city = input("Enter city name: ").strip()

        if not city:
            print("City name cannot be empty.")
            continue

        get_weather(city)

        if input("Check another city? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    main()
