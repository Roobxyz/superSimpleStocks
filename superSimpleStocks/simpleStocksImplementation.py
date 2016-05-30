import time
import operator
import math
import collections
from simpleStocks import *

class GBCE_exchange(object):

    """GBCE_exchange is a class which emulates an active exchange
        it takes an argument of an array of stocks (static reference data) 
        and simulates trades on those stocks.
        Class also contains group metrics (such as vwap and index calculation) 
        and some sorting/subset selection on the trades"""
    
    def __init__(self, static_stock_data , trades = None ):

        self.static_stock_data = static_stock_data
        
        if trades is None:
            trades = []
            self.trades = trades
            self.generate_trades( 10 )

    def __str__(self):
        trades_string=[str(i) for i in self.trades]
        return('\n'.join(trades_string))

    def generate_trades(self , n):
        """Mehtod to 'publish' n more trades to the GBCE_exchange instace """
        for i in xrange(n):
            trading_stock = random.choice( self.static_stock_data )
            price = float(random.uniform( 0, 100))
            qty = 10 * random.randint( 1, 10 )

            if random.random() > 0.5:
                self.trades.append( trading_stock.buy(price = price, qty = qty) )
            else:
                self.trades.append( trading_stock.sell(price = price, qty = qty) )
    
    def get_trades_by_sym(self, sym, trades = None):   
        """Method to return trades on a specific sym"""
        if trades is None:
            trades = self.trades
        return [trade for trade in trades if (lambda x : x.stock.sym)(trade)  == sym]

    def get_trades_asof(self, time, trades = None):   
        """Method to return trades asof a given time"""
        if trades is None:
            trades = self.trades
        
        return [trade for trade in trades if (lambda x : x.timestamp)(trade) >= time]

    def sort_trades(self, attr, reverse = True):
        """Method to sort trades by a particular attribute of the underlying class"""
        return sorted(self.trades, key=operator.attrgetter(attr), reverse=reverse)

    def vwap( self, sym ):
        """Method to calculate and return the Volume Weighted Average Price (VWAP)
        utilizes get_trades_by_sym and get_trades_asof Methods
        takes sym as argument and returns vwap for sym ( for trades as of 5 mins ago )"""
      
        trades = self.get_trades_by_sym( sym )
        five_mins_ago = datetime.datetime.now() - datetime.timedelta( minutes = 5 )
        trades = self.get_trades_asof( time = five_mins_ago, trades = trades )
        vwap_amt=0
        tot_qty = sum( [ t.qty for t in trades] )
        print 'vwap: %s total units of  %s ' % (tot_qty, sym)
        print 'vwap: %s trades on %s ' % (len(trades), sym)
        for trade in trades:
            vwap_amt += (trade.price * trade.qty) / tot_qty
        print 'vwap: vwap for %s : %s' % (sym, vwap_amt)
        return vwap_amt

    def GBCE_index(self):
        """ Method to compute and return the GBCE_index. Defined as the arithmetic mean of the :func:`vwap` of each traded sym"""
        print('Getting GBCE index via arithmetic mean')
        traded_syms = set([i.stock.sym for i in self.trades])
        n = len(traded_syms)
        if n == 0:
            print 'No trades!'
            return 0
        GBCE_index_multiplier = 1
        for sym in traded_syms:
            GBCE_index_multiplier *= self.vwap( sym )
        print 'GBCE index : %s' % (math.pow( GBCE_index_multiplier, 1./n))
        return math.pow( GBCE_index_multiplier, 1./n)

