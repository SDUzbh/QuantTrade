"""
数据加载模块：用于读取行情、财务、因子等各种数据
"""

from typing import Any, Dict, List
import pandas as pd


class DataLoader:
    def __init__(self, config: Dict[str, Any]):
        """初始化数据加载器"""
        self.config = config

    def load_price_data(self, symbols: List[str], start: str, end: str) -> pd.DataFrame:
        """
        加载价格数据
        """
        pass

    def load_factor_data(self, factor_name: str) -> pd.DataFrame:
        """
        加载某个因子数据
        """
        pass
