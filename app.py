from flask import Flask, flash, redirect, render_template, \
    request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# 主页路由
@app.route('/')
def index():
    return render_template('index.html')


# 计算器路由
@app.route('/calculate.html', methods=['GET', 'POST'])
def addition():
    error = None
    if request.method == 'POST':

        if len(request.form['firstNum']) == 0 or \
                len(request.form['secondNum']) == 0:
            flash('Input the numbers please!')
        else:
            result = int(request.form['firstNum']) + int(request.form['secondNum'])
            # print(result)
            flash(result)
            # return redirect(url_for('/calculate.html'))
    return render_template('/calculate.html', error=error)

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
