import MetaTrader5 as mt5
from fetch import get_point

deviation = 20


point = float(get_point())


def sl_tp(order_type, sl_pips, tp_pips, price):
    is_buy = (order_type == mt5.ORDER_TYPE_BUY or order_type == mt5.ORDER_TYPE_BUY_LIMIT
              or order_type == mt5.ORDER_TYPE_BUY_STOP)

    actual_sl = sl_pips * point
    actual_tp = tp_pips * point

    sl = price - actual_sl if is_buy else price + actual_sl
    tp = price + actual_tp if is_buy else price - actual_tp

    return sl, tp
