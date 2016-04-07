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
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEFUNCTION, buffer.write)
    curl.perform()
    curl.close()

    body = buffer.getvalue()

    rawdata = body.decode('iso-8859-1').split()[2:]
    data = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}
    for i in rawdata:
        x = i.split(',')
        data['date'].append(x[0])
        data['open'].append(x[1])
        data['high'].append(x[2])
        data['low'].append(x[3])
        data['close'].append(x[4])
        data['volume'].append(x[5])
        
    return data

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Get all data available from Yahoo!'
        print 'getdata <SYMB>'
        exit()

    data = get_price(sys.argv[1], '00', '2', '1970', '03', '7', '2016')
    print data['open'][0:100]
