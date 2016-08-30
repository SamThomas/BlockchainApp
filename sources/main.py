import requests
import time
import matplotlib.pyplot as plt
import datetime

print("++++++++++++++ Btc toolkit app ++++++++++++++++")

#while 1: # Infinite loop
for y in range(1):

    # get BTC info
    response = requests.get('https://chain.so/api/v2/get_info/BTC', verify=True)

    if response.status_code == 200:
        info = response.json()
        name = info['data']['name']
        network = info['data']['network']
        blocks = info['data']['blocks']
        blocks = str(blocks)  # needs to be a string for curses to display


# Plotting the Bitcoin <=> Exchange rate using Matplotlib

# Storing bitcoin data
euro_value = []
usd_value = []

for x in range(5):

    #  get EUR prices, exchange is BTC-E
    response = requests.get('https://chain.so/api/v2/get_price/BTC/EUR', verify=True)
    if response.status_code == 200:
        info = response.json()
        # Get EUR infos
        exchangeEUR = info['data']['prices'][0]['exchange']
        currencyEUR = info['data']['prices'][0]['price_base']
        priceEUR = info['data']['prices'][0]['price']
        euro_value.append(priceEUR)
        time.sleep(1)
        current_time = datetime.datetime.now()
        print("{:%H:%M:%S}".format(current_time), "EUR", euro_value[x])
    elif response.status_code == 429:
        print("Data polling restriction from chain.so | Status code: ", response.status_code)
    else:
        print("Error while retreiving data from chain.so | Status code: ", response.status_code)

    # get USD prices, exchange is Coinbase
    response = requests.get('https://chain.so/api/v2/get_price/BTC/USD', verify=True)
    if response.status_code == 200:
        info = response.json()
        # Get USD infos
        exchangeUSD = info['data']['prices'][1]['exchange']
        currencyUSD = info['data']['prices'][1]['price_base']
        priceUSD = info['data']['prices'][1]['price']
        usd_value.append(priceUSD)
    elif response.status_code == 429:
        print("Data polling restriction from chain.so | Status code: ", response.status_code)
    else:
        print("Error while retreiving data from chain.so | Status code: ", response.status_code)

def connectToCoinbase():
    response = requests.get('https://chain.so/api/v2/get_price/BTC/USD', verify=True)

def connectToBtcE():
    response = requests.get('https://chain.so/api/v2/get_price/BTC/EUR', verify=True)

def getExchangeEUR(exchangeEUR):
    exchangeEUR = info['data']['prices'][0]['exchange']

def getPriceEUR(priceEUR):
    priceEUR = info['data']['prices'][0]['price']

def getCurrencyEUR(currencyEUR):
    currencyEUR = info['data']['prices'][0]['price_base']

def getExchangeUSD(exchangeUSD):
    exchangeUSD = info['data']['prices'][1]['exchange']

def getPriceUSD(priceUSD):
    priceUSD = info['data']['prices'][1]['price']

def getCurrencyUSD(currencyUSD):
    currencyUSD = info['data']['prices'][1]['price_base']


# PLOTS
fig1 = plt.figure()
# red dashes, blue squares and green triangles
plt.plot(euro_value, 'r--', usd_value, 'bs')
plt.title('Exchange rate Bitcoins EUR')
plt.xlabel('time')
plt.ylabel('EUR')
plt.grid(True)
plt.show()
