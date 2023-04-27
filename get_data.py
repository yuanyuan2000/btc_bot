import ccxt
import pandas as pd
from ta import add_all_ta_features
from ta.trend import SMAIndicator, EMAIndicator
import IPython

def fetch_ohlcv_data(exchange, symbol, timeframe, limit):
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(data, columns=header)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def add_sma_and_ema(data, column_name, window):
    sma_indicator = SMAIndicator(data[column_name], window=window)
    ema_indicator = EMAIndicator(data[column_name], window=window)
    data[f'sma_{window}'] = sma_indicator.sma_indicator()
    data[f'ema_{window}'] = ema_indicator.ema_indicator()

def get_data():
    exchange = ccxt.kraken()
    symbol = 'BTC/AUD'
    timeframe = '1d'  # 1 day candles
    limit = 720

    data = fetch_ohlcv_data(exchange, symbol, timeframe, limit)
    data_with_ta = add_all_ta_features(data, open="open", high="high", low="low", close="close", volume="volume")
    
    # Add SMA and EMA for the close price with a 20-days window
    add_sma_and_ema(data_with_ta, 'close', 20)
    
    #test comment
