"""
回测指标计算实现
"""

import pandas as pd
import numpy as np


def compute_total_return(nav: pd.Series) -> float:
    return nav.iloc[-1] / nav.iloc[0] - 1


def compute_annualized_return(nav: pd.Series, periods_per_year: int = 252) -> float:
    total_return = compute_total_return(nav)
    n_periods = len(nav)
    return (1 + total_return) ** (periods_per_year / n_periods) - 1


def compute_max_drawdown(nav: pd.Series) -> float:
    rolling_max = nav.cummax()
    drawdown = (nav - rolling_max) / rolling_max
    return drawdown.min()
