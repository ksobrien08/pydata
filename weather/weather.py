#python3 -u "/Users/KB/Desktop/nothing/at/pydata/weather/weather.py"
#---------------------------------------------------------------------------------------
##If city exist then update
import requests, json, weatherdb as wdb
result = input("Start with a clean database? (y/n) \n")
if result == "y" or result == "Y" or result == "yes" or result == "Yes":
    wdb.delete_db()
elif result == "n" or result == "N" or result == "no" or result == "No":
    print("Think of a city name.")
else:
    print("Invalid input")
    exit()


# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
with open('config.json') as key:
    config = json.load(key)

api_key = config['api_key']

# Replace 'city_name' with the name of the city you want to get weather details for
city_name = input("What city do you want to get weather details for? \n")

# Construct the API request URL
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
else:
    # Parse the JSON response
    data = response.json()

    # Extract the relevant weather details
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    F = (temperature - 273.15) * 9/5 + 32
    humidity = data['main']['humidity']

    # Print the weather details
    print(f"Weather in {city_name}:")
    print(f"Description: {weather}")
    print(f"Temperature: {round(F, 2)} F")
    print(f"Humidity: {humidity}%")

    print("Lets add this location to our database")
   
    wdb.weather_db(city_name, weather, F, humidity)
    