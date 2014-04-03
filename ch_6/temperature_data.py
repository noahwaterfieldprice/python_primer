# Exercise 6.22
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


def get_city_codes(citylist_filename):
    infile = open(citylist_filename, 'r')
    for i in range(260):
        infile.readline()  # skip everything before content

    city_filenames = {}
    while True:
        line = infile.readline()
        if not line:                        # exit loop at end of file
            break
        if line.find('mso-list') != -1:     # check line contains country name
            city = line.split('<b>')[1][:-7]
            infile.readline()               # skip a line
            line = infile.readline()        # read in next line
            city_filename = line.split(
                '>')[1][:line.split('>')[1].find('.txt') + 4]
            city_filenames[city] = city_filename
    infile.close()

    return city_filenames


def load_city_data(city, city_filenames, subfolder='city_temp'):
    filepath = subfolder + '/' + city_filenames[city]

    # load data and create datetime object array to store dates
    month, day, year, temperature = np.loadtxt(filepath, unpack=True)
    temperature = np.loadtxt(filepath, usecols=(3,), dtype=float)
    date = [dt.datetime(y, m, d) for y, m, d in
            zip(year.astype(int), month.astype(int), day.astype(int))]
    date = np.asarray(date)
    # store in dictionary (filtering out entries with missing data)
    valid = temperature != -99
    city_data = {'name': city,
                 'date': date[valid],
                 'temperature': temperature[valid]}

    return city_data


def plot_city_data(*city_data_dicts):
    cities = []
    for city_data in city_data_dicts:
        cities.append(city_data['name'])
        plt.plot_date(city_data['date'], city_data['temperature'], '.')
    plt.ylabel('Temperature (C)')
    plt.xlabel('Date')
    plt.ylim([0, 110])
    plt.legend(cities)
    plt.show()

city_filenames = get_city_codes('city_temp/citylistWorld.htm')
Buenos_Aires_data = load_city_data('Buenos Aires', city_filenames)
London_data = load_city_data('London', city_filenames)
Reykjavik_data = load_city_data('Reykjavik', city_filenames)
Beirut_data = load_city_data('Beirut', city_filenames)
plot_city_data(Buenos_Aires_data, London_data, Reykjavik_data, Beirut_data)
