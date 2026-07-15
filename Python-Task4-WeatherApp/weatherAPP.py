import requests

print("Welcome to the Weather App")

API_KEY = "308ce4818a99d8eb7114165b18bd202f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    while True:
        city = input("\nEnter city name: ").strip()

        if city == "":
            print("Please enter a city name.")
            continue

        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                city_name = data["name"]
                country = data["sys"]["country"]
                temperature = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"].title()
                wind_speed = data["wind"]["speed"]

                print("        WEATHER REPORT")
                print(f" City        : {city_name}, {country}")
                print(f" Condition   : {description}")
                print(f" Temperature : {temperature}°C")
                print(f" Feels Like : {feels_like}°C")
                print(f" Humidity   : {humidity}%")
                print(f" Wind Speed : {wind_speed} m/s")

            elif response.status_code == 404:
                print(" City not found. Please try again.")

            elif response.status_code == 401:
                print(" Invalid API Key.")

            else:
                print(f"Error: {response.status_code}")

        except requests.exceptions.RequestException:
            print(" Network error. Please check your internet connection.")

        while True:
            again = input("\nDo you want to check another city? (yes/no): ").strip().lower()

            if again == "yes":
                break

            elif again == "no":
                print("\nThank you for using the Weather App. ")
                return

            else:
                print("Please enter yes or no.")


get_weather()
