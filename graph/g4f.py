#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
matplotlib FuncAnimation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fname = __file__.split('/')[1]
gifname = fname.replace(".py", ".gif")

ax = None

# グラフの変化を管理
i = 0

def makeFigure():
    fig = plt.figure()

    # figure() のタイトル
    fig.suptitle(fname)

    return fig

def makeAxes(fig):
    global ax
    ax = fig.add_subplot(1,1,1)
    return ax

def setAppearance():

    ax.legend(loc='upper left')

    # axesタイトル
    ax.set_title("$y=sin(x)$")

    # x軸, y軸
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # グラフの表示範囲（定義域、値域）
    ax.set_xlim([-np.pi, np.pi])
    ax.set_ylim([-1.5, 1.5])

# この関数が何度も呼ばれることでグラフの動きを表示
def makeGraph(data):
    global i

    # ax は前回の内容を保持したままなので、最初に初期化
    ax.cla()

    x = np.linspace(-np.pi, np.pi, 100)
    y = np.sin(x - np.radians(i * 10))

    ax.plot(x, y, color='g', label='$y=sin(x)$')

    # 初期化しているので、見た目ももう一回セットする。
    setAppearance()

    i += 1
    if i >= 36:
        i = 0

if __name__ == "__main__":

    fig = makeFigure()
    ax = makeAxes(fig)

    ani = animation.FuncAnimation(fig, makeGraph, interval=100)

    # gif で保存する場合は imagemagick を別途インストールしてmatplotlibrc ファイルを修正
    ani.save('./img/' + gifname, writer='imagemagick')

    plt.show()
