from app.PickStrategies import get_stock_list_all, get_strategy_stock_info, get_historical_strategy_stock_value
from flask import render_template, flash, redirect, request
from app import app
from pprint import pprint
import json


@app.route('/invest', methods=['GET', 'POST'])
def invest():
    if request.method =='POST':
        try:
            amount = float(request.form['amount'])
        except ValueError:
            return render_template('404.html', errorMsg="Invalid input stock value",)

        if amount < 5000:
            return render_template('404.html', errorMsg="Please input stock value above 5000")
        pprint(amount)
        choices = request.form['seletedStrategies']
        pprint(choices)
        choices = json.loads(choices)
        if len(choices) <= 0 or len(choices) > 2:
            return render_template('404.html')

        stocklist = get_stock_list_all(choices)
        stockInfo = get_strategy_stock_info(stocklist, amount)
        pprint(stocklist)
        stockHistInfo = get_historical_strategy_stock_value(stocklist, amount)
        return render_template("output.html", stockInfo=stockInfo, stockHistInfo=stockHistInfo)

        # try:
        #     amount = float(request.form['amount'])
        #     if amount < 5000:
        #         return render_template('error.html')
        #     pprint(amount)
        #     choices = request.form.getlist('strategies')
        #     if len(choices) <= 0 or len(choices) > 2:
        #         return render_template('error.html')
        #     pprint(choices)
        #     # testArray = ['Ethical']
        #     stocklist = get_stock_list_all(choices)
        #     details = get_strategy_stock_info(stocklist, amount)
        #     pprint(stocklist)
        #     history = get_historical_strategy_stock_value(stocklist, amount)
        #     pprint(history)
        #     return render_template("result.html", details=details, history=history)
        # except:
        #     return render_template('error.html') 

    return render_template('index.html')