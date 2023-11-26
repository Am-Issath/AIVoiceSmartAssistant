# weather_functions.py

import pyowm

def get_weather(api_key, lat, lon):
    owm = pyowm.OWM(api_key)
    observation = owm.weather_manager().weather_at_coords(lat, lon)
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    status = weather.status
    return f"The weather is {status} with a temperature of {temperature} degrees Celsius."

def number_to_words(number):
    words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }
    
    # Handle multi-digit numbers
    if number.isdigit():
        return ' '.join(words[digit] for digit in number)
    else:
        return number
