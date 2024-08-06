from flask import Blueprint, request

from initialize import init
from Order.market_order import send_market_order
from Order.pending_order import send_pending_order
from Order.modify_position import check_position
from Order.calculator import calculate_order_lot

order_bp = Blueprint('order', __name__)

init()


@order_bp.route('/market', methods=['POST'])
def market_order():
    data = request.json
    lot = data.get("lot")
    order_type = data.get("orderType")
    sl = data.get("sl")
    tp = data.get("tp")

    return send_market_order(lot, order_type, sl, tp)


@order_bp.route("/pending", methods=['POST'])
def pending_order():
    data = request.json
    lot = data.get("lot")
    entry_price = data.get("entryPrice")
    order_type = data.get("orderType")
    sl = data.get("sl")
    tp = data.get("tp")

    return send_pending_order(lot, order_type, entry_price, sl, tp)


@order_bp.route("/check/position/open", methods=['PUT'])
def check_position_open():
    data = request.json
    if "tickets" in data:
        tickets = data.get("tickets")
        for ticket in tickets:
            check_position(ticket.get("id"), ticket.get("breakeven"))


@order_bp.route("/calculator/lot", methods=['POST'])
def calculator_lot():
    data = request.json
    print(data)
    if "tradeRisk" in data and "sl" in data:
        trade_risk = data.get("tradeRisk")
        sl = data.get("sl")
        return calculate_order_lot(trade_risk, sl)
    return "Cannot calculate lot"
