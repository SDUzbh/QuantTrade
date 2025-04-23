"""
日志工具：统一的日志记录工具
"""

import logging


def setup_logger(name: str = "quant_logger", log_file: str = "log.txt") -> logging.Logger:
    """
    设置日志记录器
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(fh)

    return logger
