#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:18:13 2018

@author: changhengchen
"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("../data/AAPL.csv")
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show() # must be called to show plots

    df = pd.read_csv("../data/IBM.csv")
    print(df['High'])
    df['High'].plot()
    plt.show()

    df[['Close','Adj Close']].plot()
    plt.show()


if __name__ == "__main__":
    test_run()
