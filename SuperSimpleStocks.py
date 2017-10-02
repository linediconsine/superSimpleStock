
# coding: utf-8

# ## Structure (Dataframe) created:
# StockData [ Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value,Ticker Price]
# Trade  [Timestamp, Stock Symbol, Quantity, Buy/Sell, Price]
#
# ## Functions:
# addTrade(TimeStamp,Symbol,Quantity,Buy_Sell,Price)
# CalculateDividedYield(Symbol)
# CalculatePEratio(Symbol)
# CalculateStockPrice(Symbol)
# CalculateGeometricMean(Symbol)
# CalculateGBCE()

# Import Python Library used:
import pandas as pd,datetime,calendar,time,random
from scipy.stats.mstats import gmean
# VISUAL
from IPython.display import display


# ## Create Dataframes:
StockData = pd.read_csv("StockExample.csv").fillna(0);
StockData.set_index(['Stock Symbol']);
StockData.index = StockData['Stock Symbol'];
StockData['Ticker Price'] = -1

Trade = pd.read_csv("TradeData.csv").fillna(0);
Trade.set_index(['Stock Symbol','Timestamp']);


# ## Functions
def addTrade(TimeStamp,Symbol,Quantity,Buy_Sell,Price):
    Trade.loc[len(Trade)]=[TimeStamp,Symbol,Quantity,Buy_Sell,Price]
    StockData.loc[(Symbol,'Ticker Price')] = Price


def CalculateDividedYield(Symbol):
    TickerPrice = StockData.loc[(Symbol,'Ticker Price')]
    LastDividedYield = StockData.loc[(Symbol,'Last Dividend')]
    FixedDividend = StockData.loc[(Symbol,'Fixed Dividend')]
    FixedDividend = float(StockData.loc[('GIN','Fixed Dividend')].replace("%",""))

    if(TickerPrice == -1):
        print("! CalculateDividedYield:Warining las TickerPrice of ",Symbol,"not defined")
        return -1
    if(FixedDividend != 0):
        ParValue = StockData.loc[('GIN','Par Value')]
        DividentYieldPreferred = (( float(ParValue) / 100 )  * float(FixedDividend)) / float(TickerPrice)
    if(LastDividedYield == 0):
        print("! CalculateDividedYield:Warining Last Dividend of ",Symbol,"is 0")
        return -1

    return TickerPrice / LastDividedYield

def CalculatePEratio(Symbol):
    TickerPrice = StockData.loc[(Symbol,'Ticker Price')]
    DividedYield = CalculateDividedYield(Symbol)

    if(TickerPrice == -1):
        print("! CalculatePEratio:Warining las TickerPrice of ",Symbol,"not defined")
        return -1

    if(DividedYield == -1):
        print("! CalculatePEratio:Warining Divided Yield of ",Symbol," not found")
        return -1

    if(DividedYield == 0):
        print("! CalculatePEratio:Warining Divided Yield of ",Symbol," is 0")
        return -1

    return TickerPrice / DividedYield


def CalculateStockPrice(Symbol):
    Time15MinAgo = calendar.timegm(time.gmtime()) - datetime.timedelta(minutes=15).total_seconds()
    TradeLast15ms = Trade[Trade['Stock Symbol'] == Symbol][Trade['Timestamp'] > Time15MinAgo]
    numTrade = len(TradeLast15ms)

    if(numTrade > 0 ):
        sumTradeXqty = 0
        sumQty = 0

        for idx in range(0, numTrade):
            sumTradeXqty += TradeLast15ms.iloc[idx -1]['Price'] * TradeLast15ms.iloc[idx]['Quantity']
            sumQty += TradeLast15ms.iloc[idx-1]['Quantity']
        return sumTradeXqty / sumQty
    else:
        return 0

def CalculateGeometricMean(Symbol):
    return gmean(Trade[Trade['Stock Symbol'] == Symbol]['Price'])

def CalculateGBCE():
    GBCE = {}
    StockSymbols = Trade['Stock Symbol'].unique()
    numSymbols = len(StockSymbols)

    for idx in range(0, numSymbols):
        symbol = StockSymbols[idx -1]
        TradeSymbol = Trade[Trade['Stock Symbol'] == symbol]
        numTrade = len(TradeSymbol)
        if(numTrade > 0 ):
            sumTradeXqty = 0
            sumQty = 0

            for id2 in range(0, numTrade):
                sumTradeXqty += TradeSymbol.iloc[id2 -1]['Price'] * TradeSymbol.iloc[id2]['Quantity']
                sumQty += TradeSymbol.iloc[id2-1]['Quantity']
            if(sumQty == 0):
                print("! CalculateGBCE:Warining sumQty of ",symbol," is 0")
                GBCE[symbol] = -1
            else:
                GBCE[symbol] = sumTradeXqty / sumQty
    return GBCE
