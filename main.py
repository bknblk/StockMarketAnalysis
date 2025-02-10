import requests as r
from sys import argv
from datetime import date

headers = {
'content-type' : 'application/json; charset=utf-8',
'server' : 'Kestrel',
'lang' : 'en',
'srctype' : 'default',
'rid' : 'bd54fee9-52f5-4aee-b25b-7221444de080',
'gid' : '204',
'x-edgeconnect-midmile-rtt' : '31',
'x-edgeconnect-origin-mex-latency' : '210',
'cache-control' : 'max-age=0, no-cache, no-store',
'pragma' : 'no-cache',
}


def test():
    req = r.get('https://api.nasdaq.com/api/quote/aapl/historical?assetclass=stocks&fromdate=2020-02-02&limit=9999', headers = headers, timeout = 10)

    print(req.json())
    print(date.today())

test()

