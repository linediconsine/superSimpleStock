# superSimpleStock

I used Pandas library and other Data science library for develop this assignment.

# Files

__Jupyter/Python__
interactive version of superSimpleStock

https://github.com/linediconsine/superSimpleStock/blob/master/Marco-SuperSimpleStocks.ipynb

__uperSimpleStocks.py__
Python version

__testit.py__
Testing code for SuperSimpleStocks.py

__setup.py__ 
Should install all requirements for SuperSimpleStocks.py

# About financial languages:
Ticker Price = the last know price of a Stock
Dividend is usual referred to Last Dividend
p = price

# DataFrame:

I created 2 different DataFrame

1) StockData : Contains informations about the Stock as:
StockData [ Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value,Ticker Price]

2) Trade : Record a transactions about every stock
Trade  [Timestamp, Stock Symbol, Quantity, Buy/Sell, Price]

# Functions:
```
addTrade(TimeStamp,Symbol,Quantity,Buy_Sell,Price)
Record a transaction

CalculateDividedYield(Symbol)
Calculated Dividend Yield using provided formulas

CalculatePEratio(Symbol)
Calculated PE ratio using provided formulas

CalculateStockPrice(Symbol)
Calculated Stock Price using provided formulas

CalculateGeometricMean(Symbol)
Calculated Geometric Mean using provided formulas

CalculateGBCE()
Calculated GBCE using provided formulas for each stocks and return a dictionary
```
