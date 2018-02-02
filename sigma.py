# -*- coding: utf-8 -*-
from rqalpha.api import *
from rqalpha import run_func
import numpy as np

def init(context):
    context.stocks = sector('Energy')  

def handle_bar(context, bar_dict):
    std = []
    for it in context.stocks:
        his = history_bars(it, 100, '1d', 'close')
        if len(his) >10 and his[-1]>0:
            tem = his[1:].copy()
            ok = True
            for h in range(len(tem)):
                if his[h] <=0:
                    logger.info('here is some problems. '+str(his[h]))
                    ok = False
                    break
                tem [h] =  (tem[h] - his[h])/his[h]   #percentage growth

            if not ok:
                continue
            tem = np.array(tem)
            tem = tem * 100
            std.append(np.std(tem))
    logger.info('the result is:')
    logger.info(np.mean(std))
                
############################################################################################
config = {
    "base": {
        "start_date": "2017-10-09",
        "end_date": "2017-10-09",
        "matching_type": "current_bar",
        "benchmark": None,
        "accounts": {
            "stock": 1000000
        }
    },
    "extra": {
        "log_level": "verbose",
        "user_system_log_disabled": False,
        "user_log_disabled": False
    },
    "mod": {
        "sys_analyser": {
            "enabled": True,
            "plot": False
        }
    }
}
# 您可以指定您要传递的参数
run_func(init=init, handle_bar=handle_bar, config=config)
