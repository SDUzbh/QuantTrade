"""
订单执行模块：模拟或实盘下单
"""

import pandas as pd


class OrderExecutor:
    def __init__(self, mode: str = "backtest"):
        """
        mode: backtest / live
        """
        self.mode = mode

    def execute(self, orders: pd.DataFrame) -> pd.DataFrame:
        """
        模拟或实盘执行订单
        """
        pass
