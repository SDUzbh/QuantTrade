"""
策略基类：所有策略应继承此类
"""

import pandas as pd
from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        根据输入数据生成交易信号
        """
        pass
