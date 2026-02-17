from bot.client import BinanceFuturesClient
import logging

client = BinanceFuturesClient()

def create_order(symbol, side, order_type, quantity, price=None):

    order_data = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order_data["price"] = price
        order_data["timeInForce"] = "GTC"

    response = client.place_order(**order_data)
    return response
