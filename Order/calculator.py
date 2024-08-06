import MetaTrader5 as mt5


def calculate_order_lot(trade_risk, sl):
    acc_info = mt5.account_info()

    trade_amount = acc_info.balance * (trade_risk / 100)
    return str(trade_amount / sl)
