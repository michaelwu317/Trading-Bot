import alpaca_trade_api as tradeapi

#keys definition
public_key = '' #protected
secret_key = '' #protected
api_url = 'https://paper-api.alpaca.markets' 
api = tradeapi.REST(key_id= public_key, secret_key=secret_key, base_url=api_url) 