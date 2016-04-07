import sys
from getprice import get_price
import numpy as np

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Get all data available from Yahoo!'
        print 'getdata <SYMB>'
        exit()

    data1 = get_price(sys.argv[1], '00', '2', '1970', '03', '7', '2016')
    data2 = get_price(sys.argv[2], '00', '2', '1970', '03', '7', '2016')
    x = data1['close'][0:100]
    y = data2['close'][0:100]

    print np.corrcoef(x,y)[0][1]
