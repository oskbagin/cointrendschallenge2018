from flask import request
from datetime import datetime

class FormValidator:
    # {'end-date': ['2018-06-04'], 'plot': 
    # ['btcusd', 'ethusd', 'ltcusd'], 
    # 'start-date': ['2018-06-19']}
    def parseFormFieldToDate(self, form, date):
        tmp = form[date]
        # parse to datetime object
        tmp = datetime.strptime(str(tmp[0]), "%Y-%m-%d")

        tmp = self.testStopDate(tmp)

        return tmp

    def testStartDate(self, date):
        if date > datetime.today():
            return False
        else:
            return True

    def testStopDate(self, date):
        today = datetime.today()

        if date > today:
            return today
        else:
            return date

    def __init__(self, form):
        self.myForm = dict(form)
        self.dateStart = self.parseFormFieldToDate(self.myForm, 'start-date')
        self.dateStop = self.parseFormFieldToDate(self.myForm, 'end-date')
        self.cryptoToPlot = self.myForm['plot']
        self.datesOk = self.testStartDate(self.dateStart)
        self.timeRange = self.myForm['time-range']

        
        

    



    
        
