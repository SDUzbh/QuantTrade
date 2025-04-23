# Factor Pool 模块文档

## 功能简介
Factor Pool 模块包含不同的因子，用户可以根据这些因子进行策略构建，因子包括动量因子、估值因子等。

## 文件结构
- `base_factor.py`: 因子基类，所有因子都应继承自此类。
- `factor_momentum.py`: 动量因子。
- `factor_value.py`: 估值因子。

## 类：BaseFactor

### 方法：`compute(self, data)`
计算因子值。
- `data`: 输入的数据（DataFrame 格式）。
- 返回值：计算出的因子值（Series 格式）。

---

## 类：MomentumFactor

### 方法：`__init__(self, lookback)`
初始化动量因子。
- `lookback`: 回溯期（整数）。

### 方法：`compute(self, data)`
计算动量因子。
- `data`: 输入的数据（DataFrame 格式）。
- 返回值：计算出的动量因子值（Series 格式）。

---

## 类：ValueFactor

### 方法：`__init__(self, method)`
初始化估值因子。
- `method`: 估值方法，例如 PE 或 PB。

### 方法：`compute(self, data)`
计算估值因子。
- `data`: 输入的数据（DataFrame 格式）。
- 返回值：计算出的估值因子值（Series 格式）。
