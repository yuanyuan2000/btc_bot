import numpy as np
import pandas as pd
from ta.momentum import RSIIndicator

class Asset:
    def __init__(self):
        self.money = 100
        self.tax = 0.02
        self.coin = 0

    def buy(self):
        money_in_market = self.money * (1 - self.tax)  # add conversion AUD -> bitcoin
        self.money = 0
        return money_in_market

    def sell(self, money_in_market):
        self.money = money_in_market * (1 - self.tax)  # add conversion bitcoin -> AUD

    def trade(self, data: pd.DataFrame, windowsize, highthreshold, lowthreshold):
        in_position = False
        rsi = RSIIndicator(data["close"], window=windowsize)
        data["rsi"] = rsi.rsi()

        for i in range(len(data) - 1):
            if not in_position and data["rsi"].iloc[i] < lowthreshold:
                # Buy
                self.coin = self.buy() / data['close'].iloc[i + 1]
                in_position = True
                print(f'Buy at the {i} day')
            elif in_position and data["rsi"].iloc[i] > highthreshold:
                # Sell
                self.sell(self.coin * data['close'].iloc[i + 1])
                self.coin = 0
                in_position = False
                print(f'Sell at the {i} day. Now we have {self.money} AUD.')

        # Final sell at the end of the period
        if in_position:
            self.sell(self.coin * data['close'].iloc[-1])
            self.coin = 0

        return self.money
