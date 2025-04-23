"""
引擎模块的单元测试
"""

import unittest
import pandas as pd
from core.engine import Engine
from core.data_loader import DataLoader
from strategy_pool.mean_reversion import MeanReversionStrategy
from core.order_executor import OrderExecutor


class TestEngine(unittest.TestCase):
    def setUp(self):
        """初始化测试环境"""
        dummy_data = pd.DataFrame({
            'price': [100, 102, 101, 99, 98, 100]
        })
        self.data_loader = DataLoader(config={})
        self.strategy = MeanReversionStrategy(window=3)
        self.executor = OrderExecutor(mode="backtest")
        self.engine = Engine(
            data_loader=self.data_loader,
            strategy=self.strategy,
            executor=self.executor
        )

    def test_backtest_runs(self):
        """测试回测能否正常运行"""
        # 这里只是形式上示例，实际会需要 mock 数据加载
        try:
            self.engine.run_backtest()
        except Exception as e:
            self.fail(f"Backtest failed with exception: {e}")
