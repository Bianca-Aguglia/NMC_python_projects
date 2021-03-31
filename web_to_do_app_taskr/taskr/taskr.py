import sqlite3

from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config.from_object('_config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE_FILE'])

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error = error)
        else:
            session['logge_in'] = True
            flash('Welcome')
            return redirect(url_for('tasks'))
    return render_template('login.html')