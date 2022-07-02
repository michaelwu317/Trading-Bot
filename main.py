import alpaca_trade_api as tradeapi
import json
from config import *
import requests
import logging
import pandas


base_url = 'https://paper-api.alpaca.markets'
account_url = "{}/v2/accounts".format(base_url)
orders_url = "{}/v2/orders".format(base_url)
#r = requests.get
#continuous block
#logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
#def get_accounts():
#r = requests.get(account_url, headers = {'APCA-API-KEY-ID': public_key, 'APCA-API-SECRET-KEY': secret_key})
account = api.get_account()

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol":symbol,
        "qty":qty,
        "side":side,
        "type":type,
        "time_in_force": time_in_force
    } 
    r = requests.post(orders_url, json=data, headers=headers)
    return json.loads(r.content)

print(aapl.df)

print(account)

