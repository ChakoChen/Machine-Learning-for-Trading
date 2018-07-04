#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:16:02 2018

@author: changhengchen
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files"""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])
    return df

def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels"""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Price", fontsize=12)
    plt.show()

def compute_daily_return(df):
    """Compute and return the daily return values"""
    daily_returns = df.copy() # copy given DataFrame to match size and column name
    # compute daily returns for row 1 onwards
    daily_returns[1:] = (df[1:]/df[:-1].values) - 1
    # set daily returns for row 0 to 0
    daily_returns.iloc[0,:] = 0 
    return daily_returns

def compute_daily_return2(df):
    """Compute and return the daily return values using Pandas' DataFrame"""
    daily_returns = (df/df.shift(1)) - 1
    daily_returns.iloc[0,:] = 0 # Pandas leaves the 0th row full of NaNs
    return daily_returns

def compute_cumulative_return(df):
    cum_returns = df.copy()
    cum_returns = (df/df.iloc[0,:]) - 1 # IMPORTANT
    return cum_returns

def test_run():
    """Compute daily return"""
    # Read data
    dates = pd.date_range('2017-04-01','2017-04-30')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    
    # Do NOT forget .values to access the underlying ndarray in dataframe
    daily_ret = df['SPY'][1:]/df['SPY'][:-1].values - 1 
    
    # Plot SPY data, retain matplotlib axis object
    ax = daily_ret.plot(title='SPY Daily Return', label='SPY')
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Price", fontsize=12)
    ax.legend(loc='upper left')
    plt.show()
    
    
    """Multiple stock returns"""
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    
    #daily_returns = compute_daily_return(df)
    daily_returns = compute_daily_return2(df)
    ax = daily_returns.plot(title='Daily Return')
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Daily Return", fontsize=12)
    ax.legend(loc='lower left')
    plt.show()
    
    cum_returns = compute_cumulative_return(df)
    ax = cum_returns.plot(title='Cumulative Return')
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Cumulative Return", fontsize=12)
    ax.legend(loc='lower left')
    plt.show()
    
    
if __name__ == "__main__":
    test_run()