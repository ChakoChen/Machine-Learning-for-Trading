#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:18:17 2018

@author: changhengchen
"""

"""Scatter plots"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#from mpl_toolkits.basemap import Basemap

from util import get_data, plot_data

def compute_daily_returns(df):
    """Compute and return the daily return values"""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    daily_returns.iloc[0,:]= 0 # set daily returns for row 0 to 0
    return daily_returns

def test_run():
    dates = pd.date_range('2017-03-15', '2018-03-15')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df, title="Stock Price", xlabel="Date", ylabel="Price")
    
    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", xlabel="Date", ylabel="Daily returns")    

    """(2.1) Scatterplot SPY vs XOM """
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    
    # make sure no nan values are used for polyfit
    idx = np.isfinite(daily_returns['SPY']) & np.isfinite(daily_returns['XOM'])
    
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'][idx], daily_returns['XOM'][idx], 1) # degree 1: y = b*x + a
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')
    
    print("beta_XOM =", beta_XOM)
    print("alpha_XOM =", alpha_XOM)
    
    """(2.2) Scatterplot SPY vs GLD """
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    idx = np.isfinite(daily_returns['SPY']) & np.isfinite(daily_returns['GLD'])
    
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'][idx], daily_returns['GLD'][idx], 1)
    plt.plot(daily_returns['SPY'], beta_GLD*daily_returns['SPY'] + alpha_GLD, '-', color='r')

    print("beta_GLD =", beta_GLD)
    print("alpha_GLD =", alpha_GLD)
    
    
    """(3) Correlation"""
    print(daily_returns.corr(method='pearson'))

    
if __name__ == "__main__":
    test_run()
