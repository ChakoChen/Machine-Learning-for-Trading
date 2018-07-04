#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:38:05 2018

@author: changhengchen
"""

import pandas as pd

def test_run():
    #Define date range
    start_date = '2018-02-22'
    end_date = '2018-02-26'
    dates = pd.date_range(start_date, end_date)
    
    #Create an empty dataframe
    df1 = pd.DataFrame(index=dates)

    #Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("../data/SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date','Adj Close'],
                        na_values=['nan'])
    
    #Rename 'Adj Close' column to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
    
    #Join the two dataframes using DataFrame.join(), with how='inner'
    df1 = df1.join(dfSPY,how='inner')
    
    #Read in more stocks
    symbols = ['GOOG','IBM','GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("../data/{}.csv".format(symbol), index_col="Date",
                              parse_dates=True, usecols=['Date','Adj Close'],
                              na_values=['nan'])
        
        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df1 = df1.join(df_temp) #use default how='left'
        
    print(df1)
    
    
if __name__ == "__main__":
    test_run()