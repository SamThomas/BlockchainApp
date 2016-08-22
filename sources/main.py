import sys
from Tools.scripts.treesync import raw_input
import requests
import time
import matplotlib

print("++++++++++++++ Bbtcdash ++++++++++++++++")

while 1: # Infinite loop

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

matplotlib.test()