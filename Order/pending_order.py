import MetaTrader5 as mt5

from Order.convertor import order_type_convertor
from Order.order_tool import order_req, order_check_and_send, check_symbol_info


def send_pending_order(lot, order_type, entry_price, sl, tp):
    check_symbol_info()
    mt5_order_type = order_type_convertor(order_type)

    req = order_req(mt5.TRADE_ACTION_PENDING, lot, mt5_order_type, entry_price, sl, tp)

    return order_check_and_send(req)
