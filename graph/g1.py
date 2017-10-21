#!/usr/bin/env python
# -*- coding: utf-8 -*-
# g1.py
"""
matplotlib lineplot
"""
import numpy as np
import matplotlib.pyplot as plt

# -2 <= x <= 2 の範囲での y=x^2 のグラフ
x = np.linspace(-2, 2, 100)
y = x ** 2

plt.plot(x, y)
plt.show()
