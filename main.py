import argparse
import pyfiglet
import requests
from simple_chalk import chalk
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()
# Base URL for openweathermap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Map the weather codes to weather icons
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

# Construct url api with query parameter

parser = argparse.ArgumentParser(description="Check the weather for certain city")
parser.add_argument("Country", help="The country or city to check the weather for")
args = parser.parse_args()


url = f"{BASE_URL}?q={args.Country}&appid={os.getenv('API_KEY')}&units=metric"

# Make API request and parse response using requests module
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()
# Parsing the json response from the API and extract weather information
data = response.json()
# get information
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
desc = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct the output with weather icons
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {desc}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels Like: {feels_like}°C\n"

# Print the output
print(chalk.green(output))
