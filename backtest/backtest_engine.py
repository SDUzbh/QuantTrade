"""
回测引擎实现
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

    def run(self, data: pd.DataFrame) -> pd.Series:
        """
        回测主流程：
        1. 生成信号
        2. 组合调仓
        3. 模拟交易
        4. 计算净值
        返回：净值序列
        """
        # Step 1: 策略生成交易信号
        signals = self.strategy.generate_signals(data)

        # Step 2: PortfolioManager生成调仓权重
        weights = self.portfolio.rebalance(signals)

        # Step 3: 模拟执行
        # 此处我们构造简单订单格式，未来可扩展
        orders = pd.DataFrame({
            'date': signals.index,
            'weight': weights
        }).set_index('date')

        executed = self.executor.execute(orders)

        # Step 4: 计算净值
        nav = self.portfolio.calculate_nav(data['price'])

        return nav
