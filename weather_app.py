!pip install requests

import requests

api_key = 'YOUR API KEY' #give your API key
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
    response = requests.get(url)
    return response.json()

def print_weather_info(weather_data, city):
    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    print(f"Weather in {city}: {weather}")
    print(f"Temperature in {city}: {temp}°F")

def main():
    city = input("Enter city: ")
    weather_data = get_weather_data(city)
    print_weather_info(weather_data, city)

if __name__ == "__main__":
    main()
