"""
回测结果指标计算模块
"""

import pandas as pd


def compute_total_return(nav: pd.Series) -> float:
    """
    计算总收益
    """
    pass


def compute_annualized_return(nav: pd.Series, periods_per_year: int = 252) -> float:
    """
    计算年化收益
    """
    pass


def compute_max_drawdown(nav: pd.Series) -> float:
    """
    计算最大回撤
    """
    pass
