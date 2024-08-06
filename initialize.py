import MetaTrader5 as mt5
from credentials import login, server, passwd, path


def init():
    if not mt5.initialize(login=login, server=server, password=passwd, path=path):
        print("initialize() failed, error code =", mt5.last_error())
        raise Exception("initialize() failed, error code =", mt5.last_error())
