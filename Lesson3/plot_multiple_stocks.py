#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:12:25 2018

@author: changhengchen
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
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

def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe"""
    return df/df.iloc[0,:] ### positional indexing 

def plot_data(df, title="Stock prices"):
    '''Plot stock prices'''
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel("Date", fontsize=10)
    ax.set_ylabel("Price", fontsize=10)
    plt.show() #must be called to show plots in some environments
    
def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    df_selected = df.loc[start_index:end_index, columns]
    plot_data(df_selected, title="Selected data")
    
def test_run():
    # Define a date range
    dates = pd.date_range('2017-03-16','2018-03-16')
    
    # Choose stock symbols to read
    symbols = ['GOOG','IBM','GLD']
    
    # Get stock data
    df = get_data(symbols, dates) 
    
    '''
    # (1) Slice by row range (dates) using DataFrame.ix[] selector
    # .ix is deprecated. Please use .loc for label based indexing or .iloc for positional indexing
    print(df.loc['2017-05-01':'2017-05-31']) # the month of August
    
    # (2) Slice by column (symbols)
    print(df['GOOG'])        # a single lable selects a single column
    print(df[['IBM','GLD']]) # a list of labels selects multiple columns
    
    # (3) Slice by row and column
    print(df.loc['2017-05-01':'2017-05-31',['SPY','IBM']])
    '''
    
    # (4) Plot data
    plot_data(df)
    plot_selected(df, ['SPY','IBM'], '2017-05-01','2017-05-31')
    
    df = normalize_data(df)
    plot_data(df)
    plot_selected(df, ['SPY','IBM'], '2017-05-01','2017-05-31')

if __name__ == "__main__":
    test_run()