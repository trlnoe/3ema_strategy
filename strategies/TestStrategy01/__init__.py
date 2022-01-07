from jesse.strategies import Strategy, cached
import jesse.indicators as ta
from jesse import utils


class TestStrategy01(Strategy):

    @property
    def short_ema(self):
        return ta.ema(self.candles, 20)

    @property
    def long_ema(self):
        return ta.ema(self.candles, 40)

    def should_long(self) -> bool:
        return self.short_ema > self.long_ema

    def should_short(self) -> bool:
        return False

    def should_cancel(self) -> bool:
        return True

    def go_long(self):
        entry_price = self.price
        qty = utils.size_to_qty(self.balance, entry_price)
        self.buy = qty, entry_price

    def update_position(self) -> None:
        if self.short_ema <= self.long_ema:
            self.liquidate()

    def go_short(self):
        pass
