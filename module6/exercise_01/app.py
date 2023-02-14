from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


@app.get('/')
def index():
    dt = datetime.now()
    dt_string = dt.strftime(
        weekdays[dt.weekday()] + ', ' + months[dt.month - 1] + ' %d, %Y %H:%M:%S')
    return render_template('index.html', time=dt_string)
