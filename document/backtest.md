# Backtest 模块文档

## 功能简介
Backtest 模块负责执行策略的回测，包括模拟策略在历史数据中的表现，计算回测结果的各种绩效指标，并进行可视化。

## 文件结构
- `backtest_engine.py`: 回测引擎，负责回测的执行逻辑。
- `metrics.py`: 计算回测绩效指标。
- `visualizer.py`: 用于可视化回测结果。

## 类：BacktestEngine

### 方法：`__init__(self, strategy, portfolio, executor)`
初始化回测引擎。
- `strategy`: 策略对象。
- `portfolio`: 投资组合管理对象。
- `executor`: 订单执行对象。

### 方法：`run(self, data)`
运行回测，返回资金净值（NAV）。
- `data`: 历史数据，通常是一个 DataFrame 格式。
- 返回值：回测期间每个时间点的净值。

---

## 类：Metrics

### 方法：`compute_total_return(nav)`
计算回测的总收益。
- `nav`: 净值序列。
- 返回值：总收益百分比。

### 方法：`compute_annualized_return(nav, periods_per_year=252)`
计算回测的年化收益。
- `nav`: 净值序列。
- `periods_per_year`: 每年的交易日数量（默认252）。
- 返回值：年化收益率。

### 方法：`compute_max_drawdown(nav)`
计算回测的最大回撤。
- `nav`: 净值序列。
- 返回值：最大回撤百分比。

---

## 类：Visualizer

### 方法：`plot_nav(nav)`
绘制净值曲线。
- `nav`: 净值序列。
- 返回值：无（直接显示图表）。
