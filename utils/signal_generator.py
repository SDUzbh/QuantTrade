"""
信号生成器：用于组合多个因子或策略信号
"""

import pandas as pd
from typing import List


def combine_factors(factor_list: List[pd.Series], method: str = "rank") -> pd.Series:
    """
    将多个因子合成一个信号
    """
    pass


def generate_trade_signals(combined_score: pd.Series, threshold: float = 0.7) -> pd.Series:
    """
    根据合成打分生成最终交易信号
    """
    pass
