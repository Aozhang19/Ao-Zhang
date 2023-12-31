# Weather_Analysis

import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# OpenWeatherMap API key
api_key = '6b119c98eb252c0a393a782b1cf907e7'
city_name = 'Baltimore'

# Obtain weather data
def get_weather_data(api_key, city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data['list']

weather_data = get_weather_data(api_key, city_name)

# Extract weather information
dates = [entry['dt_txt'] for entry in weather_data]
temperatures = [entry['main']['temp'] for entry in weather_data]
weather_conditions = [entry['weather'][0]['description'] for entry in weather_data]

# Get Data Frame
df = pd.DataFrame({'Date': dates, 'Temperature': temperatures, 'Weather Condition': weather_conditions})

# Convert date format
df['Date'] = pd.to_datetime(df['Date'])

# Data analysis and visualization
plt.figure(figsize=(10, 6))

# Plot temperature curve
plt.plot(df['Date'], df['Temperature'], label='Temperature (°C)')

# Add scatter plot for weather conditions
plt.scatter(df['Date'], df['Temperature'], c='red', marker='o', label='Weather Condition')

# Add legend
plt.legend()

# Set plot title and labels
plt.title(f'Weathear Analysis for {city_name}')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')

# Automatically adjust date format
plt.gcf().autofmt_xdate()

# Show the plot
plt.show()
