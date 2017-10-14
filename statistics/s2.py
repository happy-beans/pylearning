#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def norm(ar):
    return ar / np.linalg.norm(ar)

if __name__ == "__main__":

    ar = [15,25,4,43,35,64,54,7,84,49]
    br = [15,25,4,43,35,64,54,7,84,49]
    cr = np.zeros(10)
    dr = [15,5,4,23,35,36,54,7,84,49]

    arn = norm(ar)
    brn = norm(br)
    # crn = norm(cr) // 零ベクトルは当たり前だが正規化できない。
    drn = norm(dr)

    v1 = arn.dot(brn)
    v2 = arn.dot(cr)
    v3 = arn.dot(drn)

    # 同一ベクトルを比較
    # 相関係数 = 1
    print ("{name} = {value}".format(name="correl(ar, br)", value=v1))

    # 0ベクトルとの比較
    print ("{name} = {value}".format(name="correl(ar, cr)", value=v2))

    # 要素の違うベクトルとの比較
    print ("{name} = {value}".format(name="correl(ar, dr)", value=v3))
