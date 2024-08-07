import MetaTrader5 as mt5
import eventlet
from candle import ohlct, symbol


def get_real_time_rate(sio, timeframe, channel):
    prev_timestamp = None
    prev_close = None


    while True:
        rate = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1)
        if rate:
            rate_item = rate.item()
            timestamp = int(rate_item[0])
            [o, h, l, c, t] = ohlct(rate_item)

            is_new = False

            if prev_timestamp is None:
                prev_timestamp = timestamp
                prev_close = c

            else:
                if prev_timestamp != timestamp:
                    prev_timestamp = timestamp
                    prev_close = c
                    is_new = True

            if c != prev_close or is_new:
                prev_close = c



                body = {
                    "isNew": is_new,
                    "open": o,
                    "high": h,
                    "low": l,
                    "close": c,
                    "timestamp": t,
                }

                sio.emit(channel, body)
                # print(f"{channel}: {body}")

        eventlet.sleep(0.5)

