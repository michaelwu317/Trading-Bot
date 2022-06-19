import alpaca_trade_api as tradeapi
from config import *
import requests

base_url = "https://paper-api.alpaca.markets"
account_url = "{}/v2/accounts".format(base_url)
orders_url = "{}/v2/orders".format(base_url)
#r = requests.get
#continuous block
while True:
    x = 1
    