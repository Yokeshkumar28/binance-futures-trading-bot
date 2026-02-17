from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(self.api_key, self.api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **kwargs):
        try:
            logging.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logging.info(f"Order response: {response}")
            return response
        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            raise
