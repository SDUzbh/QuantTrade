"""
绩效评估工具
"""

import pandas as pd


def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    计算夏普比率
    """
    pass


def calculate_drawdown(nav: pd.Series) -> pd.Series:
    """
    计算最大回撤
    """
    pass


def calculate_ic(factor: pd.Series, returns: pd.Series) -> float:
    """
    计算信息系数（IC）
    """
    pass
