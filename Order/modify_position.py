import MetaTrader5 as mt5

from fetch import symbol

ACTION_POSITION_CLOSE = "ACTION_POSITION_CLOSE"
ACTION_POSITION_OPEN = "ACTION_POSITION_OPEN"
ACTION_POSITION_MODIFY = "ACTION_POSITION_MODIFY"


def get_position_by_ticket(ticket):
    position = mt5.positions_get(ticket=ticket)
    print(f"position: {position}")

    return position if position else ACTION_POSITION_CLOSE


def modify_sl(ticket, new_sl):
    return {
        "action": mt5.TRADE_ACTION_SLTP,
        "position": ticket,
        "symbol": symbol,
        "sl": new_sl,
    }


def position_result(ticket, action):
    return {
        "action": action,
        "ticket": ticket,
    }


def is_order_type(order_type):
    return order_type == "BUY" or order_type == "BUY_LIMIT" or order_type == "BUY_STOP"


def check_position(ticket, breakeven, order_type):
    position = get_position_by_ticket(ticket)

    if position == ACTION_POSITION_CLOSE:
        return position_result(ticket, ACTION_POSITION_CLOSE)

    symbol_info = mt5.symbol_info_tick(symbol)
    price = symbol_info.bid
    is_buy = is_order_type(order_type)
    is_breakeven = price > breakeven if is_buy else price < breakeven

    if is_breakeven:
        req = modify_sl(ticket, breakeven)
        result = mt5.order_send(req)

        return position_result(ticket, ACTION_POSITION_OPEN)

        # if result.retcode == mt5.TRADE_RETCODE_DONE:
        #     return position_result(ticket, ACTION_POSITION_OPEN)
        #
        # else:
        #     return position_result(ticket, ACTION_POSITION_OPEN)
