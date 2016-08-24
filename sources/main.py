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

    # get USD prices, exchange is Coinbase
    response = requests.get('https://chain.so/api/v2/get_price/BTC/USD', verify=True)
    if response.status_code == 200:
        info = response.json()
        exchangeUSD = info['data']['prices'][1]['exchange']
        currencyUSD = info['data']['prices'][1]['price_base']
        priceUSD = info['data']['prices'][1]['price']
    #
    #  get EUR prices, exchange is BTC-E
    response = requests.get('https://chain.so/api/v2/get_price/BTC/EUR', verify=True)
    if response.status_code == 200:
        info = response.json()
        exchangeEUR = info['data']['prices'][0]['exchange']
        currencyEUR = info['data']['prices'][0]['price_base']
        priceEUR = info['data']['prices'][0]['price']

    print(time.strftime("%a, %d %b %Y %H:%M:%S"))

    print("Name:", name)
    print("Network:", network)
    print("Blocks:", blocks)
    print("Exchange EUR", exchangeEUR)
    print("Exchange USD: ", exchangeUSD)
    print("Price: USD", priceUSD)
    print("Price: EUR", priceEUR)

# Plotting the Bitcoin <=> Exchange rate using Matplotlib

# Storing bitcoin data
euro_value = []

for x in range(30):
    #  get EUR prices, exchange is BTC-E
    response = requests.get('https://chain.so/api/v2/get_price/BTC/EUR', verify=True)
    if response.status_code == 200:
        info = response.json()
        priceEUR = info['data']['prices'][0]['price']
        euro_value.append(priceEUR)

        time.sleep(1)
        current_time = datetime.datetime.now()
        print("{:%H:%M:%S}".format(current_time), "EUR", euro_value[x])
    else:
        print("Error while retreiving data from chain.so | Status code: ", response.status_code)


fig1 = plt.figure()
plt.plot(euro_value)
plt.title('Exchange rate Bitcoins EUR')
plt.xlabel('time')
plt.ylabel('EUR')
plt.grid(True)
plt.show()
