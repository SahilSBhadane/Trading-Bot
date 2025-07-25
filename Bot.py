from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.basicConfig(filename='bot.log', level=logging.INFO, 
                            format='%(asctime)s %(levelname)s:%(message)s')

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market Order: {order}")
            print(f"Market Order Placed: {order}")
        except Exception as e:
            logging.error(f"Market Order Error: {e}")
            print(f"Error placing market order: {e}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logging.info(f"Limit Order: {order}")
            print(f"Limit Order Placed: {order}")
        except Exception as e:
            logging.error(f"Limit Order Error: {e}")
            print(f"Error placing limit order: {e}")
