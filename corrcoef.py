import sys
from getprice import getprice
import numpy as np
import time

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'find the correlation between two symbols'
        print 'corrcoef <SYMB1> <SYMB2> <days>'
        exit()

    today = time.strftime("%d/%m/%Y")
    data1 = getprice(sys.argv[1], '02/1/1970', today)
    data2 = getprice(sys.argv[2], '02/1/1970', today)
    if len(sys.argv) == 4:
        days = int(sys.argv[3])
    else:
        days = 100
    x = data1['close'][0:days]
    y = data2['close'][0:days]

    print np.corrcoef(x,y)[0][1]
