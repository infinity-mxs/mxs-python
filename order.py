# from flask import Blueprint, request
# import MetaTrader5 as mt5
# from fetch import symbol
# from initialize import init
#
# order_bp = Blueprint('order', __name__)
#
# init()
#
# deviation = 20
#
#
# @order_bp.route('/market', methods=['POST'])
# def place_market_order():
#     data = request.json
#     lot = data.get("lot")
#     order_type = data.get("order_type")
#     sl = data.get("sl")
#     tp = data.get("tp")
#     return send_market_order(mt5.TRADE_ACTION_DEAL, lot, order_type, sl, tp)
#
#
# def action_convertor(action):
#     if action == "MARKET":
#         return mt5.TRADE_ACTION_DEAL
#     elif action == "PENDING":
#         return mt5.TRADE_ACTION_PENDING
#     else:
#         raise ValueError("Invalid action")
#
#
# def order_type_convertor(order_type):
#     if order_type == "BUY":
#         return mt5.ORDER_TYPE_BUY
#     elif order_type == "SELL":
#         return mt5.ORDER_TYPE_SELL
#     elif order_type == "BUY_LIMIT":
#         return mt5.ORDER_TYPE_BUY_LIMIT
#     elif order_type == "SELL_LIMIT":
#         return mt5.ORDER_TYPE_SELL_LIMIT
#     else:
#         raise ValueError("Invalid order_type")
#
#
# def market_order_request(action, lot, order_type, price, sl_pips, tp_pips):
#     sl = price - sl_pips if order_type == mt5.ORDER_TYPE_BUY else price + sl_pips
#     tp = price + tp_pips if order_type == mt5.ORDER_TYPE_BUY else price - tp_pips
#
#     return {
#         "action": action,
#         "symbol": symbol,
#         "volume": lot,
#         "type": order_type,
#         "price": price,
#         "sl": sl,
#         "tp": tp,
#         "deviation": deviation,
#         "magic": 234000,
#         "comment": "",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }
#
#
# def pending_order_request(lot, order_type, entry_price, current_price, sl_pips, tp_pips):
#     sl = current_price - sl_pips if order_type == mt5.ORDER_TYPE_BUY_LIMIT else current_price + sl_pips
#     tp = current_price + tp_pips if order_type == mt5.ORDER_TYPE_BUY_LIMIT else current_price - tp_pips
#
#     return {
#         "action": mt5.TRADE_ACTION_PENDING,
#         "symbol": symbol,
#         "volume": lot,
#         "type": order_type,
#         "price": entry_price,
#         "sl": sl,
#         "tp": tp,
#         "deviation": deviation,
#         "magic": 234000,
#         "comment": "",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }
#
#
# def send_pending_order(lot, order_type, entry_price, sl, tp):
#     symbol_info = mt5.symbol_info_tick(symbol)
#     if not symbol_info:
#         print(f"Failed to get symbol info for {symbol}")
#         return
#
#     price = symbol_info.ask
#
#     mt5_order_type = order_type_convertor(order_type)
#
#     order_req = pending_order_request(lot, mt5_order_type, entry_price, price, sl, tp)
#
#     result = mt5.order_send(order_req)
#     print(mt5.last_error())
#
#     if result.retcode != mt5.TRADE_RETCODE_DONE:
#         print(f"OrderSend failed, retcode={result.retcode}")
#         return f"Failed to place order, retcode: {result.retcode}"
#     else:
#         print(f"OrderSend successful, order_id={result.order}")
#         return "Order place successfully"
#
#
# print(send_pending_order(1.0, "BUY_LIMIT", 2352.45, 100, 100))
#
#
# def send_market_order(action, lot, order_type, sl, tp):
#     symbol_info = mt5.symbol_info_tick(symbol)
#     if not symbol_info:
#         print(f"Failed to get symbol info for {symbol}")
#         return
#
#     price = symbol_info.ask
#
#     mt5_action = action_convertor(action)
#     mt5_order_type = order_type_convertor(order_type)
#
#     order_req = market_order_request(mt5_action, lot, mt5_order_type, price, sl, tp)
#
#     result = mt5.order_send(order_req)
#     print(mt5.last_error())
#
#     if result.retcode != mt5.TRADE_RETCODE_DONE:
#         print(f"OrderSend failed, retcode={result.retcode}")
#         return f"Failed to place order, retcode: {result.retcode}"
#     else:
#         print(f"OrderSend successful, order_id={result.order}")
#         return "Order place successfully"
#
