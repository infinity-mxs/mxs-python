import dataclasses

symbol = "XAUUSD"


@dataclasses.dataclass
class Candle:
    open: float
    high: float
    low: float
    close: float
    timestamp: int


def ohlct(rate):
    o = float(rate[1])
    h = float(rate[2])
    l = float(rate[3])
    c = float(rate[4])
    t = int(rate[0])

    return o, h, l, c, t
