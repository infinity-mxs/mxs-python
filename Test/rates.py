import MetaTrader5 as mt5
from fetch import symbol
from candle import Candle, ohlct
import datetime


def get_historical_candles(timeframe):
    candles = []

    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 2000)

    counter = 0
    for rate in rates:
        rate_item = rate.item()

        [o, h, l, c, t] = ohlct(rate_item)

        if counter == 0:
            print(f"First candle: {datetime.datetime.fromtimestamp(t)}")
            counter += 1

        candle = Candle(o, h, l, c, t)
        print(candle)
        candles.append(candle)

    return candles


candles = get_historical_candles(mt5.TIMEFRAME_M5)

print(f"index 0: {datetime.datetime.fromtimestamp(candles[0].timestamp)}")
