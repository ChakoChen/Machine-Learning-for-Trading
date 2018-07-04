#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:13:34 2018

@author: changhengchen
"""

import pandas as pd

def get_mean_volume(symbol):
    """
    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv(("../data/{}.csv").format(symbol)) # read in data
    return df['Volume'].mean() # compute and return max

def test_run():
    """Function called by Test Run."""
    print("Mean volume")
    for symbol in ['AAPL', 'IBM']:
        print(symbol, get_mean_volume(symbol))


if __name__ == "__main__": # if run standalone
    test_run()
