
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

# Importing
import pandas as pd,datetime,calendar,time,random
from scipy.stats.mstats import gmean
# VISUAL
from IPython.display import display


# Create Dataframes:
StockData = pd.read_csv("StockExample.csv").fillna(0);
StockData.set_index(['Stock Symbol']);
StockData.index = StockData['Stock Symbol'];
StockData['Ticker Price'] = -1

Trade = pd.read_csv("TradeData.csv").fillna(0);
Trade.set_index(['Stock Symbol','Timestamp']);


# Functions
def addTrade(TimeStamp,Symbol,Quantity,Buy_Sell,Price):
    Trade.loc[len(Trade)]=[TimeStamp,Symbol,Quantity,Buy_Sell,Price]
    StockData.loc[(Symbol,'Ticker Price')] = Price


def CalculateDividedYield(Symbol):
    TickerPrice = StockData.loc[(Symbol,'Ticker Price')]
    LastDividedYield = StockData.loc[(Symbol,'Last Dividend')]
    FixedDividend = float(str(StockData.loc[(Symbol,'Fixed Dividend')]).replace("%",""))

    if(TickerPrice == -1):
        print("! CalculateDividedYield:Warining las TickerPrice of ",Symbol,"not defined")
        return -1
    if(FixedDividend != 0):
        ParValue = StockData.loc[(Symbol,'Par Value')]
        DividentYieldPreferred =  (( float(ParValue) / 100 )  * float(FixedDividend)) / float(TickerPrice)
        return DividentYieldPreferred
    if(LastDividedYield == 0):
        # I want 0 / int = 0
        return 0

    return TickerPrice / LastDividedYield

def CalculatePEratio(Symbol):
    TickerPrice = StockData.loc[(Symbol,'Ticker Price')]
    LastDivided = StockData.loc[(Symbol,'Last Dividend')]

    if(TickerPrice == -1):
        print("! CalculatePEratio:Warining las TickerPrice of ",Symbol,"not defined")
        return -1

    if(LastDivided == -1):
        print("! CalculatePEratio:Warining Divided Yield of ",Symbol," not found")
        return -1

    if(LastDivided == 0):
        print("! CalculatePEratio:Warining Divided Yield of ",Symbol," is 0")
        return 0

    return TickerPrice / LastDivided


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


# Simple tests

def testIT():
    # Use clean Datasets
    StockData = pd.read_csv("StockExample.csv").fillna(0);
    StockData.set_index(['Stock Symbol']);
    StockData.index = StockData['Stock Symbol'];
    StockData['Ticker Price'] = -1

    Trade = pd.read_csv("TradeData.csv").fillna(0);
    Trade.set_index(['Stock Symbol','Timestamp']);


    TimeStamp = calendar.timegm(time.gmtime())
    addTrade(TimeStamp,'TEA',20,'Buy',20);
    # Last divident = 0
    # Ticker Price = 20
    # Expected Divided Yield = 0
    assert CalculateDividedYield('TEA') == 0

    # Testing preferred mode
    # 2% of 100 = 2
    # Ticker Price = 20
    # 2 / 20 = 0.1
    addTrade(TimeStamp,'GIN',20,'Buy',20);
    assert CalculateDividedYield('GIN') == 0.1

    # Testing P/E Ration
    # Ticker price = 20
    # Last Divident GIN = 8
    # Results = 20 / 8 = 2.5
    assert CalculatePEratio('GIN') == 2.5

    # Calculate Stock Price
    # Stock Price = sqr(20 * 20) = 20
    addTrade(TimeStamp,'GIN',20,'Buy',20);
    addTrade(TimeStamp,'GIN',20,'Buy',20);
    addTrade(TimeStamp,'GIN',20,'Buy',20);
    assert round(CalculateStockPrice('GIN'),3) == 38.182

    # Calculate GBCE
    GBCE = CalculateGBCE()
    assert round(GBCE['ALE'],3) == 155.0
    assert round(GBCE['GIN'],3) == 22.708
    assert round(GBCE['JOE'],3) == 126.0
    assert round(GBCE['POP'],3) == 105.0
    assert round(GBCE['TEA'],3) == 60.909
testIT()
