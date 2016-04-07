import sys
from getprice import get_price
import numpy as np

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Get all data available from Yahoo!'
        print 'getdata <SYMB>'
        exit()

    data = get_price(sys.argv[1], '00', '2', '1970', '03', '7', '2016')
    x = data['open'][0:10]
    print np.mean(x)
