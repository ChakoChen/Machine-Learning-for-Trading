#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:34:40 2018

@author: changhengchen
"""

"""Utility functions"""
import os
import pandas as pd

def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
        
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date",
                        parse_dates=True, usecols=['Date','Adj Close'],
                        na_values=['nan'])
    
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
    
        #df = df.join(df_temp, how='inner')
        df = df.join(df_temp)
        if symbol=='SPY': #drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
        
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2017-03-16','2018-03-16')
    
    # Choose stock symbols to read
    symbols = ['GOOG','IBM','GLD']
    
    # Get stock data
    df = get_data(symbols, dates) 
    
    # (1) Slice by row range (dates) using DataFrame.ix[] selector
    # .ix is deprecated. Please use .loc for label based indexing or .iloc for positional indexing
    print(df.loc['2017-05-01':'2017-05-31']) # the month of August
    
    # (2) Slice by column (symbols)
    print(df['GOOG'])        # a single lable selects a single column
    print(df[['IBM','GLD']]) # a list of labels selects multiple columns
    
    # (3) Slice by row and column
    print(df.loc['2017-05-01':'2017-05-31',['SPY','IBM']])
    

if __name__ == "__main__":
    test_run()