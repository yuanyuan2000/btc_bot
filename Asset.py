import numpy as np
import pandas as pd

class Asset:
    def __init__(self, parameters: list):
        self.money = 100
        self.parameters = parameters  # => ['sma_9','sma_21','ema_9','ema_21']
        self.tax = 0.02
        self.coin = 0

    def buy(self, coin_value):
        money_in_market = self.money * (1 - self.tax)  # add conversion AUD -> bitcoin
        self.money = 0
        self.coin = money_in_market / coin_value

    def sell(self, coin_value):
        self.money = (coin_value * self.coin) * (1 - self.tax)
        self.coin = 0

    # def trade(self, data: pd.DataFrame):
    #     in_position = False
    #     short_window, long_window = self.parameters

    #     for i in range(len(data) - 1):
    #         if not in_position and data[short_window].iloc[i] < data[long_window].iloc[i] and data[short_window].iloc[i + 1] > data[long_window].iloc[i + 1]:
    #             # Buy
    #             self.coin = self.buy() / data['close'].iloc[i + 1]
    #             in_position = True
    #             print(f'Buy at the {i} day')
    #         elif in_position and data[short_window].iloc[i] > data[long_window].iloc[i] and data[short_window].iloc[i + 1] < data[long_window].iloc[i + 1]:
    #             # Sell
    #             self.sell(self.coin * data['close'].iloc[i + 1])
    #             self.coin = 0
    #             in_position = False
    #             print(f'Sell at the {i} day. Now we have {self.money} AUD.')

    #     # Final sell at the end of the period
    #     if in_position:
    #         self.sell(self.coin * data['close'].iloc[-1])
    #         self.coin = 0
            

    #     return self.money



