"""
示例策略：动量策略
"""

import pandas as pd
from strategy_pool.base_strategy import BaseStrategy


class MomentumStrategy(BaseStrategy):
    def __init__(self, lookback: int = 60):
        self.lookback = lookback

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        基于动量因子生成交易信号
        """
        pass
