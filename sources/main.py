import sys
from Tools.scripts.treesync import raw_input
import requests
import time

# Blockchain.info API
from blockchain import exchangerates


ticker = exchangerates.get_ticker()

# Print the 15 min price for every currency
for k in ticker:
    print (k, ticker[k].p15min)

# Bitcoin converter

print("*************Welcome to the Bitcoin converter**************")

try:
    amount_to_be_converted = float(raw_input('Amount to be converted in Bitcoins:'))
except ValueError:
    print("Not a number")

try:
    currency_to_be_converted = input('Currency to be converted in Bitcoins: EUR, USD, GBP, JPY, CAD ')
except ValueError:
    print("Not a currency name")

btc_amount = exchangerates.to_btc(currency_to_be_converted, amount_to_be_converted)

print(btc_amount)
print("************************ END ***********************")

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
    print("Currency USD", currencyUSD)
    print("Currency EUR: ", currencyEUR)
    print("Price: USD", priceUSD)
    print("Price: EUR", priceEUR)
