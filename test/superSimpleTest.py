from superSimpleStocks.simpleStocks import *
from superSimpleStocks.simpleStocksImplementation import *

static_data = [ 
    stock('TEA','common',0,100),
    stock('POP','common',8,100),
    stock('ALE','common',23,60),
    stock('GIN','preferred',8,100,0.02),
    stock('JOE','common',13,250) ]

traded_stocks = GBCE_exchange(static_data)

for i in range(5):
    traded_stocks.generate_trades( 10 ) 
    n = len( traded_stocks.trades ) 
    #time.sleep(2) # To simulate realtime trades coming in in batches
    traded_stocks.GBCE_index()
    print ('Total trades on exchange: %s' % n)

print( str(traded_stocks) )
print( 'ALL %s TRADES SHOWN ABOVE' % len( traded_stocks.trades ) )
traded_stocks.GBCE_index()
last_trade = traded_stocks.trades[n-1]

#testing the stock clases methods
print 'last trade: %s ' % last_trade
print 'dividend yield: %s' % ( last_trade.dividend_yield() )
print 'P/E Ratio: %s' %  ( last_trade.PE_ratio() )
