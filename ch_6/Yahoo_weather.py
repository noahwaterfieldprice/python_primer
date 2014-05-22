# Exercise 6.27
# -*- coding: utf-8 -*- # Need this to display degrees sign properly
import datetime as dt
import urllib as url

week = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
d = dt.date.today().weekday()
days = ['Today', 'Tomorrow',
        week[(d + 2) % 7], week[(d + 3) % 7], week[(d + 4) % 7]]


def get_yahoo_data():
    ox_url = 'https://weather.yahoo.com/united-kingdom/england/oxford-31278/'
    infile = url.urlopen(ox_url)
    yahoo_forecast = {}
    counter = 0
    while True:
        line = infile.readline()
        if not line:  # exit loop at end of file
            break
        # check line contains weather type and read it in if so
        if line.find('"condition') != -1:
            condition = line.split()[2][3:].split('-')
            if condition[-1] == 'n':  # remove trailing n if present
                condition.pop()
            weather = ' '.join(condition).capitalize()

            # skip next 3 lines and read in max/min temperatures
            for i in range(3):
                infile.readline()
            line = infile.readline()
            max_temp = line.split('&')[0].split('>')[-1]
            line = infile.readline()
            min_temp = line.split('&')[0].split('>')[-1]

            # store in dictionary
            yahoo_forecast[days[counter]] = {'weather': weather,
                                             'max_temp': max_temp,
                                             'min_temp': min_temp}
            counter += 1
    infile.close()
    return yahoo_forecast


def print_weather_data(forecast):
    print '5-DAY FORECAST'
    print '-' * 62
    print '%-10s %-28s %-11s %-9s' % ('Day', 'Weather',
                                      'Max Temp', 'Min Temp')
    print '-' * 62
    for day in days:
        print '%-10s %-28s %-12s %-9s' % (day,
                                          forecast[day]['weather'],
                                          forecast[day]['max_temp'] + ' °C',
                                          forecast[day]['min_temp'] + ' °C')
    print '-' * 62

yahoo_forecast = get_yahoo_data()
print_weather_data(yahoo_forecast)

"""
Sample run:
python Yahoo_weather.py
5-DAY FORECAST
--------------------------------------------------------------
Day        Weather                      Max Temp    Min Temp
--------------------------------------------------------------
Today      Scattered thunderstorms      16 °C       9 °C
Tomorrow   Showers                      16 °C       8 °C
Sunday     Showers                      13 °C       6 °C
Monday     Scattered thunderstorms      15 °C       5 °C
Tuesday    Showers                      16 °C       4 °C
--------------------------------------------------------------
"""
