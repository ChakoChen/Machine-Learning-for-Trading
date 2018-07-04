#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:39:35 2018

@author: changhengchen
"""

import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("../data/AAPL.csv")

    # TODO: Print last 5 rows of the data frame
    print(df)        # all rows
    print(df.head()) # first 5 rows
    print(df.tail()) # last 5 rows
    print(df[5:11])  # rows between 5 and 10 (slicing)

if __name__ == "__main__":
    test_run()
