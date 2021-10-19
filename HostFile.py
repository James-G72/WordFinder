import pandas as pd
import sqlalchemy
from binance import BinanceSocketManager
from binance.client import Client

# api_key =
# api_secret_key =
client = Client(api_key, api_secret_key)

bsm = BinanceSocketManager(client)

socket = bsm.tade_socket("BTCUSDT")

def recieve_pack():
    socket.__aenter__()
    msg = socket.recv()
    print(msg)

recieve_pack()