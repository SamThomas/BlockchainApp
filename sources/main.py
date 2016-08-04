import sys
from Tools.scripts.treesync import raw_input

# Blockchian.info libraries
from blockchain import exchangerates


ticker = exchangerates.get_ticker()

# Print the 15 min price for every currency
for k in ticker:
    print (k, ticker[k].p15min)

# Bitcoin converter

try:
    amount_to_be_converted = float(raw_input('Amount to be converted in Bitcoins:'))
except ValueError:
    print("Not a number")

btc_amount = exchangerates.to_btc('EUR', amount_to_be_converted)
print(btc_amount)
