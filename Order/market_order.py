import MetaTrader5 as mt5

from Order.convertor import order_type_convertor
from Order.order_tool import order_check_and_send, order_req, check_symbol_info
from fetch import symbol


def send_market_order(lot, order_type, sl, tp):
    symbol_info = check_symbol_info()

    price = symbol_info.ask
    mt5_order_type = order_type_convertor(order_type)

    req = order_req(mt5.TRADE_ACTION_DEAL, lot, mt5_order_type, price, sl, tp)

    return order_check_and_send(req)
