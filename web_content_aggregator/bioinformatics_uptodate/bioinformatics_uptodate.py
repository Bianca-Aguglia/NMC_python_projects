#!usr/bin/python3
'''
Application controller for 'Bioinformatics - Up_To_Date'.
'''

from flask import Flask

app = Flask(__name__)

app.config['DATABASE'] = 

@app.route('/')
@app.route('/home')
def home():
    return 'home'

if __name__ == '__main__':
    app.run(debug=True)

