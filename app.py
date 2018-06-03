from flask import Flask, request, render_template
from flask import render_template
from datetime import time
from packets.urlDataGetter import CryptoDataGetter
from packets.formsHandler import FormValidator
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

appTitle = 'CoinTrends - Challenge 2018'
legend='BTCUSD '
labels=[]
values=[]

@app.route("/")
def chart():
    legend = ''
    return render_template('chart.html', values=values, labels=labels, legend=legend, 
        head_title = appTitle, renderChart=0)

@app.route("/", methods=['POST'])
def fetchDataFromForm():
    global labels, values

    validateForm = FormValidator(request.form)

    print(validateForm.timeRange)

    getter = CryptoDataGetter(
            validateForm.cryptoToPlot[0],
            validateForm.timeRange[0]
        )
    
    labels, values = getter.provideCryptoData(
            validateForm.dateStart,
            validateForm.dateStop
        )
    
    labels.reverse()
    values.reverse()
    
    return render_template('chart.html', values=values, labels=labels, legend=legend, 
        head_title = appTitle, renderChart=1)

if __name__ == "__main__":  
    app.run(debug=True)
