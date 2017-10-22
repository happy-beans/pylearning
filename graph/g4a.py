#!/usr/bin/env python
# -*- coding: utf-8 -*-
# g4a.py

"""
matplotlib ArtistAnimation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fname = __file__.split('/')[1]
gifname = fname.replace(".py", ".gif")

def makeFigure():
    fig = plt.figure()

    # figure() のタイトル
    fig.suptitle(fname)

    return fig

def makeAxes(fig):
    ax = fig.add_subplot(1,1,1)

    # axesタイトル
    ax.set_title("$y=sin(x)$")

    # x軸, y軸
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # グラフの表示範囲（定義域、値域）
    ax.set_xlim([-np.pi, np.pi])
    ax.set_ylim([-1.5, 1.5])

    return ax

if __name__ == "__main__":

    fig = makeFigure()
    ax = makeAxes(fig)

    # パラパラ漫画を作成（プロットされたaxが１コマ）
    ims = []
    d = 0
    for i in range(36):
        x = np.linspace(-np.pi, np.pi, 100)
        y = np.sin(x - np.radians(i * 10))

        im = ax.plot(x, y, color='b', label='$y=sin(x)$')
        if i == 0:
            ax.legend(loc='upper left')

        ims.append(im)

    ani = animation.ArtistAnimation(fig, ims, interval=100)

    # gif で保存する場合は imagemagick を別途インストールしてmatplotlibrc ファイルを修正
    ani.save('./img/' + gifname, writer='imagemagick')

    plt.show()
