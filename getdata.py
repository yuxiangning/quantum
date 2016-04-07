import sys
import pycurl
from io import BytesIO

# a : start month, 00, 01, etc.
# b : start day, 1, 2, ...
# c : start year, 1970
# d : end month
# e : end day
# f : end year
def get_price(symbol, a, b, c, d, e, f):
    url = 'http://real-chart.finance.yahoo.com/table.csv?s=' + symbol + \
        '&a=' + a + '&b=' + b + '&c=' + c + '&d=' + d + '&e=' + e + '&f=' + f + \
        '&g=d&ignore=.csv'

    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue()

    return body.decode('iso-8859-1').split()[2:]
    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Get all data available from Yahoo!'
        print 'getdata <SYMB>'
        exit()

    x = get_price(sys.argv[1], '00', '2', '1970', '03', '7', '2016')
    print x[0]
