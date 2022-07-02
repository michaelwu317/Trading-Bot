import alpaca_trade_api as tradeapi

#keys definition
public_key = '' #protected
secret_key = '' #protected
api_url =  'https://paper-api.alpaca.markets'
endpointurl = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(public_key, secret_key, api_url, api_version='v2') 
headers = {'APCA-API-KEY-ID': public_key, 'APCA-API-SECRET-KEY': secret_key}