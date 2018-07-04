#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:04:54 2018

@author: changhengchen
"""

"""Plot a histogram"""

import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data

def compute_daily_returns(df):
    """Compute and return the daily return values"""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    daily_returns.iloc[0,:]= 0 # set daily returns for row 0 to 0
    return daily_returns

def test_run():
    """Plot 1 histgram"""
    # Read data
    dates = pd.date_range('2017-03-15','2018-03-15')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df, title="Stock Price", xlabel="Date", ylabel="Price")
    
    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", xlabel="Date", ylabel="Daily returns")    
    
    # Plot a histogram
    daily_returns.hist(bins=50) # default number of bins: 10
    
    # Get mean and starndard deviation
    mean = daily_returns['SPY'].mean()
    print("mean =", mean)
    std = daily_returns['SPY'].std()
    print("std =", std)
    
    plt.axvline(mean, color='k', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)

    # Compute kurtosis
    print("kurtosis =",daily_returns['SPY'].kurtosis()) # if positive -> fat tails
    
    
    
    """Plot two histograms together"""
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df, title="Stock Price", xlabel="Date", ylabel="Price")
    
    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", xlabel="Date", ylabel="Daily returns")    
    
    # Plot histogram directly from dataframe
    plt.figure()
    #daily_returns.hist(bins=50) # two separate histgrams
    daily_returns['SPY'].hist(bins=20, label="SPY")
    daily_returns['XOM'].hist(bins=20, label="XOM")
    plt.legend(loc='upper right')
    
if __name__ == "__main__":
    test_run()
