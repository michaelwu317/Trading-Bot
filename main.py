import alpaca_trade_api as tradeapi
from config import *
import requests

base_url = "https://paper-api.alpaca.markets"
account_url = "{}/v2/accounts".format(base_url)
orders_url = "{}/v2/orders".format(base_url)
#r = requests.get
#continuous block
def get_accounts():
    r = requests.get(account_url, headers = {'APCA-API-KEY-ID': public_key, 'APCA-API-SECRET-KEY': secret_key})
while True:
    x = 1
    