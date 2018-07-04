#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:20:04 2018

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
    
def get_rolling_mean(df, window):   
    return df.rolling(window=window, center=False).mean()

def get_rolling_std(df, window):
    return df.rolling(window=window, center=False).std()

def get_bollinger_bands(rm, rstd):
    return rm+2*rstd, rm-2*rstd
    

def test_run():
    """Compute rolling mean"""
    # Read data
    dates = pd.date_range('2017-04-01','2018-2-28')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    
    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title='SPY rolling mean', label='SPY')
    
    # Compute rolling mean using a 20-day window
    #rm_SPY = pd.rolling_mean(df['SPY'], window=20) # DEPRECATED
    rm_SPY = df['SPY'].rolling(window=20, center=False).mean()
    
    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)
    
    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
    
    
    """Compute Bollinger Bands"""
    # (1) Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window=20)
    
    # (2) Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window=20)
    
    # (3) Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
    
    # Plot
    ax2 = df['SPY'].plot(title='Bollinger Bands', label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax2)
    upper_band.plot(label='Upper band', ax=ax2)
    lower_band.plot(label='Lower band', ax=ax2)
    
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Price")
    ax2.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()
    