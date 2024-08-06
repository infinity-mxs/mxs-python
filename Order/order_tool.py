import MetaTrader5 as mt5
from fetch import symbol
from Order.sl_tp import sl_tp, deviation


def order_check_and_send(req):
    result_check = mt5.order_check(req)
    if result_check.retcode == 0:
        result_send = mt5.order_send(req)

        if result_send.retcode == mt5.TRADE_RETCODE_DONE:
            return str(result_send.order)
        else:
            return str(f"Send failed, retcode: {result_send.retcode}")

    else:
        return str(f"Check failed, retcode: {result_check.retcode}")


def order_req(action, lot, order_type, price, sl_pips, tp_pips):
    [sl, tp] = sl_tp(order_type, sl_pips, tp_pips, price)

    return {
        "action": action,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": deviation,
        "magic": 234000,
        "comment": "",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }


def check_symbol_info():
    symbol_info = mt5.symbol_info_tick(symbol)
    if not symbol_info:
        print(f"Failed to get symbol info for {symbol}")
        return

    return symbol_info
