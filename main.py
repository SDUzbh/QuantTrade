"""
主程序入口：初始化组件并运行回测流程
"""

from core.data_loader import DataLoader
from core.engine import Engine
from core.order_executor import OrderExecutor
from core.portfolio import PortfolioManager
from strategy_pool.mean_reversion import MeanReversionStrategy
from backtest.backtest_engine import BacktestEngine
from backtest.visualizer import plot_nav

import pandas as pd

def main():
    # === 1. 准备假数据（实际场景请从文件或API加载） ===
    dates = pd.date_range(start='2021-01-01', periods=100)
    prices = pd.Series([100 + i * 0.2 + (i % 5 - 2) for i in range(100)], index=dates)
    data = pd.DataFrame({'price': prices})

    # === 2. 初始化模块 ===
    data_loader = DataLoader(config={})
    strategy = MeanReversionStrategy(window=5)
    executor = OrderExecutor(mode='backtest')
    portfolio = PortfolioManager(initial_capital=1_000_000)

    # === 3. 回测流程 ===
    backtest_engine = BacktestEngine(strategy, portfolio, executor)
    nav = backtest_engine.run(data)

    # === 4. 可视化输出 ===
    plot_nav(nav)


if __name__ == '__main__':
    main()
