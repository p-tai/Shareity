from humbler import app
from flask import render_template
import helpers

content = {}
charities = {}

def listContent():
    for item in content:
        print(item)

def listCharities():
    print("foo");
    for charity in charities:
        print(charity)

@app.route('/content')

@app.route('/charities')

@app.route('/url')
def addContent():
    print("url")
    return render_template('buyscreen.html')

@app.route('/addCharity', methods=['POST'])
def addCharity():
    return
    

@app.route('/', methods=['GET', 'POST'])
def index():
    """The index page"""
    listContent();
    return render_template('index.html')
