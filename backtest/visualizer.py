"""
回测可视化模块
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_nav(nav: pd.Series):
    """
    绘制净值曲线
    """
    plt.figure(figsize=(10, 4))
    plt.plot(nav, label="Net Asset Value")
    plt.title("Backtest NAV")
    plt.legend()
    plt.grid(True)
    plt.show()
