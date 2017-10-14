#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

# 合計
def getSum(ar):
    return np.sum(ar)

# 平均
def getAvg(ar):
    return np.average(ar)

# 偏差
def getDev(ar):
    a = getAvg(ar)
    d = []
    for i in ar:
        d.append(i - a)

    return d

# 分散
def getVar(ar):
    return np.var(ar)

# 標準偏差
def getStd(ar):
    return np.std(ar)

# 偏差値
def getDV(ar):
    d = getDev(ar)
    s = getStd(ar)

    dv = []
    i = 0
    for i in range(len(ar)):
        dv.append(d[i] * 10 / s + 50)

    return dv

if __name__ == "__main__":

    ar = [15,25,4,43,35,64,54,7,84,49]

    # 合計
    print("{name} = {val}".format(name='合計',val=getSum(ar)))

    # 平均
    print("{name} = {val}".format(name='平均',val=getAvg(ar)))

    # 偏差
    print("{name} = {val}".format(name='偏差',val=getDev(ar)))

    # 分散
    print("{name} = {val}".format(name='分散',val=getVar(ar)))

    # 標準偏差
    print("{name} = {val}".format(name='標準偏差',val=getStd(ar)))

    # 偏差値
    print("{name} = {val}".format(name='偏差値',val=getDV(ar)))
