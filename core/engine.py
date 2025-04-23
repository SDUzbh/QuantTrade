"""
交易引擎：调度策略、数据、执行器
"""

from typing import Any
from core.data_loader import DataLoader
from core.order_executor import OrderExecutor
from strategy_pool.base_strategy import BaseStrategy


class Engine:
    def __init__(self, data_loader: DataLoader, strategy: BaseStrategy, executor: OrderExecutor):
        """初始化引擎"""
        self.data_loader = data_loader
        self.strategy = strategy
        self.executor = executor

    def run_backtest(self):
        """
        运行回测
        """
        pass

    def run_live(self):
        """
        实盘运行
        """
        pass
