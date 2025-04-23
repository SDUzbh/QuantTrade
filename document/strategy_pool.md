# Strategy Pool 模块文档

## 功能简介
Strategy Pool 模块包含不同的策略实现，策略通过因子信号生成买卖信号，常见策略如均值回归、动量策略等。

## 文件结构
- `base_strategy.py`: 策略基类，所有策略都应继承此类。
- `mean_reversion.py`: 均值回归策略。
- `momentum.py`: 动量策略。

## 类：BaseStrategy

### 方法：`generate_signals(self, data)`
根据数据生成交易信号。
- `data`: 输入的数据（DataFrame 格式）。
- 返回值：生成的交易信号（DataFrame 格式）。

---

## 类：MeanReversionStrategy

### 方法：`__init__(self, window)`
初始化均值回归策略。
- `window`: 窗口期（整数）。

### 方法：`generate_signals(self, data)`
根据价格数据生成买卖信号。
- `data`: 输入的价格数据（DataFrame 格式）。
- 返回值：生成的买卖信号（DataFrame 格式）。

---

## 类：MomentumStrategy

### 方法：`__init__(self, lookback)`
初始化动量策略。
- `lookback`: 回溯期（整数）。

### 方法：`generate_signals(self, data)`
根据价格数据生成动量信号。
- `data`: 输入的价格数据（DataFrame 格式）。
- 返回值：生成的动量信号（DataFrame 格式）。
