import requests
from datetime import datetime

class CryptoDataGetter:
    cryptoData = []

    def __init__(self, coin='BTCUSD', timePeriod='monthly'):
        urlAddress = 'https://apiv2.bitcoinaverage.com/indices/global/history/' + \
                        coin + '?period=' + timePeriod + '&?format=json'

        r = requests.get(url=urlAddress)
        self.cryptoData = r.json()
    
    def parseStringToDatetime(self, dateString):
        tmp = dateString
        # parse to datetime object
        tmp = datetime.strptime(dateString, "%Y-%m-%d %H:%M%S")

        return tmp

    def testDate(self, dateString, startDate, endDate):
        ret = self.parseStringToDatetime(dateString)
        if ret >= startDate and ret <= endDate:
            return True

        return False

    def provideCryptoData(self, start, end):
        xData = []
        yData = []

        # {'time': '2018-06-03 17:00:00', 
        # 'high': 7710.12, 
        # 'open': 7710.12, 
        # 'low': 7683.33, 
        # 'average': 7695.99}

        for i in self.cryptoData:
            if self.testDate(i['time'][0:-3], start, end):
                xData.append(i['time'])
                yData.append(i['average'])
        
        return xData, yData

