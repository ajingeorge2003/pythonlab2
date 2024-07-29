weather_data = [
    {'Date': '2024-08-01', 'MaxTemp': 31, 'MinTemp': 22, 'Humidity': 70},
    {'Date': '2024-08-02', 'MaxTemp': 33, 'MinTemp': 23, 'Humidity': 65},
    {'Date': '2024-08-03', 'MaxTemp': 34, 'MinTemp': 24, 'Humidity': 60},
    {'Date': '2024-08-04', 'MaxTemp': 30, 'MinTemp': 21, 'Humidity': 75},
    {'Date': '2024-08-05', 'MaxTemp': 32, 'MinTemp': 22, 'Humidity': 80},
    {'Date': '2024-08-06', 'MaxTemp': 35, 'MinTemp': 25, 'Humidity': 55},
    {'Date': '2024-08-07', 'MaxTemp': 29, 'MinTemp': 20, 'Humidity': 85},
    {'Date': '2024-08-08', 'MaxTemp': 28, 'MinTemp': 19, 'Humidity': 90},
    {'Date': '2024-08-09', 'MaxTemp': 27, 'MinTemp': 18, 'Humidity': 95},
    {'Date': '2024-08-10', 'MaxTemp': 31, 'MinTemp': 22, 'Humidity': 70},
]

import random
from datetime import datetime, timedelta

start_date = datetime.strptime('2024-08-11', '%Y-%m-%d')
end_date = datetime.strptime('2024-07-10', '%Y-%m-%d')

current_date = start_date
while current_date <= end_date:
    weather_data.append({
        'Date': current_date.strftime('%Y-%m-%d'),
        'MaxTemp': random.randint(25, 35),
        'MinTemp': random.randint(15, 25),
        'Humidity': random.randint(50, 100)
    })
    current_date += timedelta(days=1)


def find_highest_and_lowest_temps(data):
    max_temp = max(data, key=lambda x: x['MaxTemp'])
    min_temp = min(data, key=lambda x: x['MinTemp'])
    return max_temp, min_temp

def days_above_30(data):
    return sum(1 for day in data if day['MaxTemp'] > 30)

def average_humidity(data):
    total_humidity = sum(day['Humidity'] for day in data)
    return total_humidity / len(data)

max_temp, min_temp = find_highest_and_lowest_temps(weather_data)
print(f"Highest Temperature: {max_temp['MaxTemp']}°C on {max_temp['Date']}")
print(f"Lowest Temperature: {min_temp['MinTemp']}°C on {min_temp['Date']}")

days_above_30_count = days_above_30(weather_data)
print(f"Number of days with temperatures above 30°C: {days_above_30_count}")

avg_humidity = average_humidity(weather_data)
print(f"Average Humidity: {avg_humidity:.2f}%")

'''
Highest Temperature: 35°C on 2024-08-06
Highest Temperature: 35°C on 2024-08-06
Lowest Temperature: 18°C on 2024-08-09
Number of days with temperatures above 30°C: 6
Lowest Temperature: 18°C on 2024-08-09
Number of days with temperatures above 30°C: 6
Number of days with temperatures above 30°C: 6
'''