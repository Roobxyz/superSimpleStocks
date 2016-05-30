import datetime
import random

#
# stock class
#
        
class stock(object):
    """Simple stock class to contain static data pertaining to a stock,
        contins fuctions which utilize external variable price to calculate metrics"""
    def __init__(self, sym, typ, ldiv, pval, fdiv = None ):
        self.sym = sym
        self.typ = typ
        self.ldiv = ldiv
        self.pval = pval
        self.fdiv = fdiv
       
    def __repr__(self):
        return 'stock(sym = %s, typ = %s, ldiv = %s, pval = %s, fdiv = %s)' % (self.sym , self.typ , self.ldiv, self.pval, self.fdiv)
    
    def __str__(self):
        return self.sym
    
    def dividend_yield(self,price):
        """Bound method, takes float argument. calculates dividend yield according to
        Dividend Yield = Last Dividend / price if common stock
        Dividend Yield = (Fixed Dividend * Par Value) / price """ 
        if self.typ == 'common':
            try:
                return self.ldiv / float(price)
            except ZeroDivisionError:
                print 'Cannot compute dividend yeild: price = 0, returning None' 
                return None

        elif self.typ == 'preferred':
            try:
                return (self.pval * self.fdiv) / float(price)
            except ZeroDivisionError:
                print 'Cannot compute dividend yeild: price = 0, returning None' 
                return None
    
    def PE_ratio(self,price):
        """Returns the price earnings ratio of a stock given a price 
        defined as price/Last Dividend"""
        try: 
            return float(price)/self.ldiv
        except ZeroDivisionError:
            print 'Cannot compute P/E ratio Last Dividend = 0, returning None' 
            return None
    
    def buy( self, price, qty, buysell='B' ):
        """ returns a 'buy' trade object on a stock instance """
        return  trade( self, price, qty, buysell )
    
    def sell( self, price, qty, buysell='S' ):
        """ returns a 'sell' trade object on a stock instance """
        return  trade( self, price, qty, buysell )



#
# trade Class
#

class trade(object):
    """simple trade class, 
    an instance will represent a trade on a given sock
    includes a time, quantity, price, buysell indicator"""
    def __init__(self, stock, price, qty, buysell,timestamp = None):
        self.stock = stock
        self.price = price
        self.qty = qty
        self.buysell = buysell
        if(timestamp is None):
            timestamp = datetime.datetime.now()
        self.timestamp = timestamp
                 
        
    def __repr__(self):    
       return 'trade(stock=%s, price=%s,  qty=%s,  buysell=%s,  timestamp=%s) ' % (self.stock, self.price, self.qty, self.buysell, self.timestamp)
    
    def __str__(self):
       return '%s %s units %s at %s | %s ' % (self.status(), self.qty, self.stock, self.price, self.timestamp)
    
    def status(self):
        """string to show if trade has been 'Bought' 'B' or 'Sold' 'S' """
        if self.buysell =='S':
            return 'Sold'
        elif self.buysell == 'B':
            return 'Bought'

    def PE_ratio(self):
        """calculates P/E ratio as given by :class:`stock` uses instance of the :class:`trade` price"""
        return self.stock.PE_ratio(self.price)

    def dividend_yield(self):
        """calculates dividend yield as given by :class:`stock` uses instance of the :class:`trade` price"""
        return self.stock.dividend_yield(self.price)
