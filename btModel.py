# -*- coding: utf-8 -*-

# run_func_demo
from rqalpha.api import *
from rqalpha import run_func
import talib


def read_csv_as_df(csv_path):    
    # 通过 pandas 读取 csv 文件，并生成 DataFrame
    import pandas as pd
    data = pd.read_csv(csv_path)
    return data


def init(context):
    import os
    # 获取当前运行策略的文件路径
    strategy_file_path = context.config.base.strategy_file
    # 根据当前策略的文件路径寻找到相对路径为 "../IF1706_20161108.csv" 的 csv 文件
    csv_path = os.path.join(os.path.dirname(strategy_file_path), "./fff.csv")
    # 读取 csv 文件并生成 df
    IF1706_df = read_csv_as_df(csv_path)
    # 传入 context 中
    context.IF1706_df = IF1706_df


def before_trading(context):
    # 通过context 获取在 init 阶段读取的 csv 文件数据
    logger.debug(context.IF1706_df)

def handle_bar(context, bar):
    #
    #order_target_value(stock, 0)
    pass



############################################################################################
config = {
    "base": {
        "start_date": "2016-06-01",
        "end_date": "2016-12-01",
        "matching_type": "current_bar",
        "benchmark": None,
        "accounts": {
            "future": 1000000
        }
    },
    "extra": {
        "log_level": "verbose",
        "user_system_log_disabled": True,
        "user_log_disabled": False
    },
    "mod": {
        "sys_analyser": {
            "enabled": True,
            "plot": True
        }
    }
}

# 您可以指定您要传递的参数
run_func(init=init, handle_bar=handle_bar, config=config)
