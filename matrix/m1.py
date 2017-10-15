#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def p(name, ar):
    print("{name} :".format(name=name))
    print("{value}".format(value=ar))
    print("")

if __name__ == "__main__":

    # サンプルの行列
    ar = np.random.randint(1,10,4).reshape(2,2)
    br = np.random.randint(1,10,4).reshape(2,2)

    # 単位行列
    I = np.identity(2)
    # 零行列
    O = np.zeros(4).reshape(2,2)

    p("ar", ar)
    p("br", br)
    p("I", I)
    p("O", O)

    p("ar + br", ar + br)
    p("ar.br", ar.dot(br))
    p("br.ar", br.dot(ar))

    p("ar.I", ar.dot(I))
    p("I.ar", I.dot(ar))

    p("ar.O", ar.dot(O))
    p("O.ar", O.dot(ar))
