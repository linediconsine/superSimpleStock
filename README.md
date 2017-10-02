# superSimpleStock

I used Pandas library to structure this exercize,
I found it easy, readable and fast.

# Files

Marco-SuperSimpleStocks.ipynb
Jupyter/Python interactive version of superSimpleStock

superSimpleStocks.py  --> Python version
testit.py --> Testing code for SuperSimpleStocks.py
scomuetup.py --> Should install all requirements for SuperSimpleStocks.py

# DataFrame:

I created 2 different DataFrame

1) StockData : Contains informations about the Stock as:
StockData [ Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value,Ticker Price]

2) Trade : Record a transactions about every stock
Trade  [Timestamp, Stock Symbol, Quantity, Buy/Sell, Price]

# About financial languages:
Ticker Price = the last know price of a Stock
Dividend is usual referred to Last Dividend
p = price

# Functions:

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
