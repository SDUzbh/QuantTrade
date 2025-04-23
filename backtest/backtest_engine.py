"""
回测引擎：用于运行策略回测
"""

import pandas as pd
from core.portfolio import PortfolioManager
from core.order_executor import OrderExecutor
from strategy_pool.base_strategy import BaseStrategy


class BacktestEngine:
    def __init__(self, strategy: BaseStrategy, portfolio: PortfolioManager, executor: OrderExecutor):
        self.strategy = strategy
        self.portfolio = portfolio
        self.executor = executor

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        运行回测，并返回资金净值或持仓记录
        """
        pass
