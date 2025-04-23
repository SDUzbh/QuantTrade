"""
示例因子：估值因子
"""

import pandas as pd
from factor_pool.base_factor import BaseFactor


class ValueFactor(BaseFactor):
    def __init__(self, method: str = "pe"):
        """
        method: 可选 'pe', 'pb' 等
        """
        self.method = method

    def compute(self, data: pd.DataFrame) -> pd.Series:
        """
        计算估值因子
        """
        pass
