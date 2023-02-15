from flask import Flask, render_template, redirect, request

app = Flask(__name__)

registrations = {}
org_options = ['49th Security Division',
               'App Ventures',
               'Charlotte Hack',
               'Game Dev',
               'Girls Who Code']


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/registrants')
def registrants():
    return render_template('registrants.html', students=registrations)


@app.post('/registrants')
def submit():
    name = request.form.get('name')
    org = request.form.get('org')

    if not name or not org or org not in org_options:
        return render_template('error.html')
    else:
        registrations[name] = org
        return redirect('/registrants', code=302)
