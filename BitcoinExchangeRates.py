
# import from blockchain library
from blockchain import exchangerates

# get the bitcoin rates in different currencies
ticker = exchangerates.get_ticker()

# print the bitcoin price in every currency
print("Bitcoin Prices")
for k in ticker:
    print(k, ticker[k].p15min)