import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for, g

app = Flask(__name__)
app.config.from_object('_config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE_FILE'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

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

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye!')
    return redirect(url_for('login'))

@app.tasks('/tasks')
@login_required
def tasks():
    g.db = connect_db()
    cursor = g.db.cursor()
    cursor.execute('SELECT name, due_date, priority, task_id FROM tasks WHERE status=0')
    open_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cursor.fetchall()]
    
    cursor.execute('SELECT name, due_date, priority, task_id FROM tasks WHERE status=1')
    closed_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cursor.fetchall()]
    
    g.db.close()
    return render_template('tasks.html',
                           form = AddTaskForm(request.form),
                           open_tasks = open_tasks,
                           closed_tasks = closed_tasks)

@app.route('/add', methods = ['POST'])
@login_required
def new_task():
    g.db = connect_db()
    name = request.form['name']
    due_date = request.form['due_date']
    priority = request.form['priority']
    if not name or not date or not priority:
        flash('All fields are required. Please try again.')
        return redirect(url_for('tasks'))
    else:
        task = (name, due_date, priority, 1)
        g.db.execute('INSERT INTO tasks VALUES (null, ?, ?, ?, ?)', task)
        g.db.commit()
        g.db.close()
    flash('New task was successfully added.')
    return redirect(url_for('tasks'))


@app.route('/complete/<int:task_id>')
@login_required
def complete(task_id):
    g.db = connect_db()
    cursor = g.db.cursor()
    cursor.execute('UPDATE tasks SET status = 0 WHERE task_id = ?', (task_id,))
    g.db.commit()
    g.db.close()
    flash('The task was marked as complete')
    return redirect(url_for('tasks'))

@app.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    g.db = connect_db()
    cursor = g.db.cursor()
    cursor.execute('DELETE FROM tasks WHERE task_id = ?', (task_id,))
    g.db.commit()
    g.db.close()
    flash('The task was deleted.')
    return redirect(url_for('tasks'))

























                        
                       
