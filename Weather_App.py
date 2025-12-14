
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["description"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print("Error connecting to the weather service:", e)

def main():
    api_key = "1bb3b886b6c2036cd81e6e58cb80eab1"  
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        get_weather(city, api_key)

if __name__ == "__main__":
    main()

