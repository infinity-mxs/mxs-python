from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
import py_eureka_client.eureka_client as eureka_client

import MetaTrader5 as mt5

from real_time_socket import get_real_time_rate
from fetch import get_historical_candles, get_prev_rate, timeframe_convertor, get_point
from Order.main import order_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(order_bp, url_prefix='/order')

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def on_connect():
    print("Connected")


@socketio.on('error')
def on_error(error):
    print(error)


@app.route('/<string:timeframe>/historical-candles', methods=['GET'])
def historical_candles(timeframe):
    return get_historical_candles(timeframe_convertor(timeframe))


@app.route("/<string:timeframe>/prev-candle", methods=['GET'])
def prev_candle(timeframe):
    return get_prev_rate(timeframe_convertor(timeframe))


@app.route("/point", methods=['GET'])
def point():
    return get_point()


if __name__ == '__main__':
    eureka_server = "http://192.168.100.20:8761/eureka"

    # Register the Flask app with Eureka
    eureka_client.init(eureka_server=eureka_server,
                       app_name='FLASK',
                       instance_port=5000)

    socketio.start_background_task(lambda: get_real_time_rate(socketio, mt5.TIMEFRAME_M1, "M1"))
    socketio.start_background_task(lambda: get_real_time_rate(socketio, mt5.TIMEFRAME_M3, "M3"))
    socketio.start_background_task(lambda: get_real_time_rate(socketio, mt5.TIMEFRAME_M5, "M5"))
    socketio.start_background_task(lambda: get_real_time_rate(socketio, mt5.TIMEFRAME_M15, "M15"))
    socketio.start_background_task(lambda: get_real_time_rate(socketio, mt5.TIMEFRAME_H1, "H1"))

    socketio.run(app, host='192.168.100.59', port=24999)
