"""
示例策略：均值回归策略
"""

import pandas as pd
from strategy_pool.base_strategy import BaseStrategy


class MeanReversionStrategy(BaseStrategy):
    def __init__(self, window: int = 20):
        self.window = window

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        价格低于移动平均时买入，高于时卖出
        """
        pass
