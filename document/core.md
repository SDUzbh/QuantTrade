# Core 模块文档

## 功能简介
Core 模块包含了数据加载、交易引擎、订单执行和投资组合管理的核心功能，支持策略的执行和资金管理。

## 文件结构
- `data_loader.py`: 数据加载器，负责从不同数据源加载价格和因子数据。
- `engine.py`: 交易引擎，负责策略调度和执行。
- `order_executor.py`: 订单执行器，模拟或实盘下单。
- `portfolio.py`: 投资组合管理器，负责资金和资产分配。

## 类：DataLoader

### 方法：`__init__(self, config)`
初始化数据加载器。
- `config`: 配置参数，包含数据源信息等。

### 方法：`load_price_data(self, symbols, start, end)`
加载指定资产的历史价格数据。
- `symbols`: 资产符号列表。
- `start`: 起始日期（字符串格式）。
- `end`: 结束日期（字符串格式）。
- 返回值：包含价格数据的 DataFrame。

### 方法：`load_factor_data(self, factor_name)`
加载某个因子的历史数据。
- `factor_name`: 因子名称。
- 返回值：因子数据的 DataFrame。

---

## 类：Engine

### 方法：`__init__(self, data_loader, strategy, executor)`
初始化交易引擎。
- `data_loader`: 数据加载器对象。
- `strategy`: 策略对象。
- `executor`: 订单执行器对象。

### 方法：`run_backtest(self)`
运行回测。
- 返回值：回测结果的净值曲线。

### 方法：`run_live(self)`
启动实盘交易。
- 返回值：无。

---

## 类：OrderExecutor

### 方法：`__init__(self, mode)`
初始化订单执行器。
- `mode`: 模式，'backtest' 或 'live'。

### 方法：`execute(self, orders)`
执行交易订单。
- `orders`: 订单数据（DataFrame 格式）。
- 返回值：执行结果的数据。

---

## 类：PortfolioManager

### 方法：`__init__(self, initial_capital)`
初始化投资组合管理器。
- `initial_capital`: 初始资金。

### 方法：`rebalance(self, signals)`
根据策略信号进行组合调仓。
- `signals`: 策略信号（DataFrame 格式）。
- 返回值：新的组合权重。

### 方法：`calculate_nav(self, price_data)`
计算净值曲线。
- `price_data`: 价格数据（DataFrame 格式）。
- 返回值：净值曲线（Series 格式）。
