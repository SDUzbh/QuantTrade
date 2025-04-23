"""
因子基类：所有因子应继承此类
"""

import pandas as pd
from abc import ABC, abstractmethod


class BaseFactor(ABC):
    @abstractmethod
    def compute(self, data: pd.DataFrame) -> pd.Series:
        """
        根据数据计算因子值
        """
        pass
