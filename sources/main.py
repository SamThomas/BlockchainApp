import sys
from Tools.scripts.treesync import raw_input

# Blockchian.info libraries
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