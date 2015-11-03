# Exercise 6.18
# Author: Noah Waterfield Price

import matplotlib.pyplot as plt


def read_file(filename):
    infile = open(filename, 'r')
    infile.readline()  # read column headings
    dates = []
    prices = []
    for line in infile:
        columns = line.split(',')
        date = columns[0]
        date = date[:-3]  # skip day of month
        price = columns[-1]
        dates.append(date)
        prices.append(float(price))
    infile.close()
    dates.reverse()
    prices.reverse()
    return dates, prices


def load_files(filelist):
    dates = {}
    prices = {}
    for filename in filelist:
        name = filename[:-4]  # read company name from 'name.csv' string
        d, p = read_file(filename)
        dates[name] = d
        prices[name] = p
    data = {'prices': prices, 'dates': dates}
    return data


def normalise_prices(prices):
    norm_prices = {}
    for company in prices:
        norm_price = prices[company][0]
        norm_prices[company] = \
            [p / norm_price for p in prices[company]]
    return norm_prices

filelist = ['Apple.csv', 'Google.csv', 'Microsoft.csv',
            'Nokia.csv', 'Sony.csv']
data = load_files(filelist)
data['norm prices'] = normalise_prices(data['prices'])

# Let the "x" values in the plot just be the indices
companies = []
for company in data['norm prices']:
    plt.plot(data['norm prices'][company], linewidth=1.5)
    companies.append(company)
plt.legend(companies, loc=2)
plt.ylabel('Stock price')
plt.xlabel('Time (months from Jan 1 2005)')
plt.title('Major corporation stock price variation - 2005-2014')
plt.show()
