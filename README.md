# superSimpleStock

I used Pandas library to structure this exercize,
I found it easy, readable and fast.

# Files

Marco-SuperSimpleStocks.ipynb --> Jupyter/Python version   
SuperSimpleStocks.py  --> Python version

# DataFrame:

I created 2 different DataFrame

1) StockData : Contains informations about the Stock as:
StockData [ Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value,Ticker Price]

2) Trade : Record a transactions about every stock
Trade  [Timestamp, Stock Symbol, Quantity, Buy/Sell, Price]

In my research about financial languages:
Ticker Price = the last know price of a Stock


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
{ Symbol : }
