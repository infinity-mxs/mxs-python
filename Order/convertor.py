import MetaTrader5 as mt5


def order_type_convertor(order_type):
    if order_type == "BUY":
        return mt5.ORDER_TYPE_BUY
    elif order_type == "SELL":
        return mt5.ORDER_TYPE_SELL
    elif order_type == "BUY_LIMIT":
        return mt5.ORDER_TYPE_BUY_LIMIT
    elif order_type == "SELL_LIMIT":
        return mt5.ORDER_TYPE_SELL_LIMIT
    else:
        raise ValueError("Invalid order_type")


def action_convertor(action):
    if action == "MARKET":
        return mt5.TRADE_ACTION_DEAL
    elif action == "PENDING":
        return mt5.TRADE_ACTION_PENDING
    else:
        raise ValueError("Invalid action")
