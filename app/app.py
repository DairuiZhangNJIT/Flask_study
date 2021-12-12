import os

from flask import Flask, flash, redirect, render_template, \
    request, url_for
import time
import pandas as pd
from calc.calculator import Calculator

app = Flask(__name__)
app.secret_key = b'sdhaosidjaoisjsikj'

cal_history_list = []


# 主页路由
@app.route('/')
def index():
    return render_template('index.html')


# 计算器路由
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':  # 点击submit button
        if len(request.form['firstNum']) == 0 or len(request.form['secondNum']) == 0:
            flash('Input the numbers please!')
        else:

            # get the values
            value1 = request.form['firstNum']
            value2 = request.form['secondNum']
            operation = request.form['operation']

            # make the tuple
            my_tuple = (value1, value2)

            # call operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            flash(result)

            # save to history
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cal_history = [t, value1, value2, operation, result]
            CSV_name = ["Time", "1stValue", "2ndValue", "Operation", "Result"]

            DataFrame = pd.DataFrame([cal_history])
            print(DataFrame)
            if not os.path.exists("cal_history.csv"):
                DataFrame.to_csv("cal_history.csv", header=CSV_name, mode='a', index=False, sep=',')
            else:
                DataFrame.to_csv("cal_history.csv", header=None, mode='a', index=False, sep=',')

            return render_template('calculate.html')
    else:
        return render_template('calculate.html')


# history路由
@app.route('/history', methods=["POST", "GET"])
def history():
    if request.method == "GET":
        data = pd.read_csv('cal_history.csv')

        cal_history_list = data.values.tolist()
        print(cal_history_list)
        return render_template("history.html", his=cal_history_list)

# 登录界面路由
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#                 request.form['password'] != 'secret':
#             error = 'Invalid credentials'
#         else:
#             flash('You were successfully logged in')
#             return redirect(url_for('index'))
#     return render_template('calculate.html', error=error)
