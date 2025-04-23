"""
示例因子：动量因子
"""

import pandas as pd
from factor_pool.base_factor import BaseFactor


class MomentumFactor(BaseFactor):
    def __init__(self, lookback: int = 60):
        self.lookback = lookback

    def compute(self, data: pd.DataFrame) -> pd.Series:
        """
        计算动量因子（当前价格 - N 日前价格）
        """
        pass
