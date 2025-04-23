# Utils 模块文档

## 功能简介
Utils 模块包含常用的工具函数，例如日志记录、绩效计算和信号生成。

## 文件结构
- `logger.py`: 日志记录工具。
- `performance.py`: 绩效评估工具。
- `signal_generator.py`: 信号生成器工具。

## 方法：`setup_logger(name, log_file)`
设置日志记录器。
- `name`: 日志名称。
- `log_file`: 日志文件路径。
- 返回值：日志记录器对象。

---

## 方法：`calculate_sharpe_ratio(returns, risk_free_rate=0.0)`
计算夏普比率。
- `returns`: 收益序列（Series 格式）。
- `risk_free_rate`: 无风险利率（浮动，默认0）。
- 返回值：夏普比率（浮动）。

---

## 方法：`calculate_drawdown(nav)`
计算最大回撤。
- `nav`: 净值曲线（Series 格式）。
- 返回值：最大回撤（浮动）。

---

## 方法：`combine_factors(factor_list, method="rank")`
合成多个因子。
- `factor_list`: 因子列表（List[Series] 格式）。
- `method`: 合成方法（'rank' 或 'sum'）。
- 返回值：合成后的因子（Series 格式）。

---

## 方法：`generate_trade_signals(combined_score, threshold=0.7)`
根据合成因子生成交易信号。
- `combined_score`: 合成得分（Series 格式）。
- `threshold`: 交易信号阈值（浮动）。
- 返回值：交易信号（Series 格式）。
