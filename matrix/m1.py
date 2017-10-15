#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":

    # サンプルの行列
    ar = np.random.randint(1,10,4).reshape(2,2)

    # 単位行列
    I = np.identity(2)

    # 零行列
    O = np.zeros(4).reshape(2,2)

    # 行列が以下で定義されるとき
    print("ar = ")
    print(ar)
    print("")
    print("I = ")
    print(I)
    print("")
    print("O = ")
    print(O)
    print("")

    # 単位行列との演算
    print("1. ar.I")
    print(ar.dot(I))
    print("")
    print("2. I.ar")
    print(I.dot(ar))
    print("")

    # 零行列との演算
    print("3. ar.O")
    print(ar.dot(O))
    print("")
    print("4. O.ar")
    print(O.dot(ar))
