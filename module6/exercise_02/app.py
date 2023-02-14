from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/calculate')
def calculate():
    possible_num = request.args.get('num')
    result = ''
    if not possible_num:
        result = 'No number provided!'
    elif not possible_num.isnumeric():
        result = possible_num + ' is not an integer!'
    else:
        possible_num = int(possible_num)
        result = str(possible_num) + ' is ' + \
            ('even' if possible_num % 2 == 0 else 'odd')

    return render_template('calculate.html', message=result)
