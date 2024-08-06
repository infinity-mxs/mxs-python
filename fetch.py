import MetaTrader5 as mt5
from candle import *
from initialize import init
import datetime

init()


def get_point():
    symbol_info = mt5.symbol_info(symbol)
    point = symbol_info.point
    return str(point)


timestamp = 1625074800

# Convert timestamp to datetime object
dt_object = datetime.datetime.fromtimestamp(timestamp)

# Format datetime object to a string
formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_date)


def get_historical_candles(timeframe):
    candles = []

    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 2000)

    counter = 0
    for rate in rates:
        print(counter)
        counter += 1
        rate_item = rate.item()

        [o, h, l, c, t] = ohlct(rate_item)

        candle = Candle(o, h, l, c, t)
        candles.append(candle)

    return candles


def get_prev_rate(timeframe):
    prev_rate = mt5.copy_rates_from_pos(symbol, timeframe, 1, 1)

    prev_rate_item = prev_rate.item()

    [o, h, l, c, t] = ohlct(prev_rate_item)

    return {
        "open": o,
        "high": h,
        "low": l,
        "close": c,
        "timestamp": t
    }


def timeframe_convertor(timeframe):
    if timeframe == "M1":
        return mt5.TIMEFRAME_M1

    elif timeframe == "M3":
        return mt5.TIMEFRAME_M3

    elif timeframe == "M5":
        return mt5.TIMEFRAME_M5

    elif timeframe == "M15":
        return mt5.TIMEFRAME_M15

    elif timeframe == "H1":
        return mt5.TIMEFRAME_H1

    else:
        raise ValueError("Undefined timeframe")
