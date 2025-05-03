"""
回测结果可视化
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_nav(nav: pd.Series):
    plt.figure(figsize=(10, 4))
    plt.plot(nav, label="Net Asset Value", color="blue")
    plt.title("Backtest Net Asset Value")
    plt.xlabel("Date")
    plt.ylabel("NAV")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
