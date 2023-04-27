import ccxt
import pandas as pd
from ta import add_all_ta_features
from ta.trend import SMAIndicator, EMAIndicator

# fetch the data from kraken and return it as a dataframe
def fetch_ohlcv_data(exchange, symbol, timeframe, limit):
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(data, columns=header)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# get the SMA for the close price with a "window" days window
def add_sma(data, column_name, window):
    sma_indicator = SMAIndicator(data[column_name], window=window)
    data[f'sma_{window}'] = sma_indicator.sma_indicator()
    return data

# get the EMA for the close price with a "window" days window
def add_ema(data, column_name, window):
    ema_indicator = EMAIndicator(data[column_name], window=window)
    data[f'ema_{window}'] = ema_indicator.ema_indicator()
    return data

# main function, returns the dataframe with all the data and technical indicators
def grab_data():
    exchange = ccxt.kraken()
    symbol = 'BTC/AUD'
    timeframe = '1d'  # 1 day candles
    limit = 720

    # Fetch the data
    data = fetch_ohlcv_data(exchange, symbol, timeframe, limit)
    
    # Add SMA and EMA for the close price with a 9-days/21-days window
    data = add_sma(data, 'close', 9)
    data = add_sma(data, 'close', 21)
    data = add_ema(data, 'close', 9)
    data = add_ema(data, 'close', 21)

    # Add all ta features
    data = add_all_ta_features(data, open="open", high="high", low="low", close="close", volume="volume")

    return data
    

