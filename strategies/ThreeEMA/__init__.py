from jesse.strategies import Strategy, cached
import jesse.indicators as ta
from jesse import utils


class ThreeEMA(Strategy):
    @property
    def short_ema(self):
        return ta.ema(self.candles, 9)

    @property
    def mid_ema(self):
        return ta.ema(self.candles, 21)

    @property
    def long_ema(self):
        return ta.ema(self.candles, 55)

    @property 
    def sma200(self):
        return ta.sma(self.candles, 200)

    @property 
    def rsi(self):
        return ta.rsi(self.candles, 14)
    @property 
    def atr(self):
        return ta.atr(self.candles, 14)

    
    def should_long(self) -> bool:
        return self.mid_ema > self.short_ema

    def should_short(self) -> bool:
        return False

    def should_cancel(self) -> bool:
        return self.short_ema < self.mid_ema

    def go_long(self):         
        qty = 0.1
        take_profit = self.price + self.atr * 3  
        stop = self.price - self.atr * 2 
        self.stop_loss = qty, stop  
        self.take_profit = qty, take_profit
        self.buy = qty, self.price, self.balance   
        

    def update_position(self) -> None: 
        if self.is_long and self.price > self.balance:
            self.liquidate() 
       

    def go_short(self):
        pass
