#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:01:59 2018

@author: changhengchen
"""

''' Build a dataframe in pandas '''
import pandas as pd


def test_run():
    # Define date range
    start_date = '2018-02-22'
    end_date = '2018-02-26'
    dates = pd.date_range(start_date, end_date)

    print(dates)
    print(dates[0])  # date time index object

    # Create an empty dataframe
    df1 = pd.DataFrame(index=dates)  # now the index is not 0, 1, 2, ...
    print(df1)  # print the index of the date time index object

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("../data/SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    # Join the two dataframes using DataFrame.join()
    #df1 = df1.join(dfSPY)

    # Drop NaN values
    #df1 = df1.dropna()

    # Instead using two lines, do the following
    df1 = df1.join(dfSPY, how='inner')  # inner join

    print(df1)


if __name__ == "__main__":
    test_run()
