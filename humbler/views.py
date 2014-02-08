from humbler import app
from flask import render_template
import helpers


@app.route('/', methods=['GET', 'POST'])
def index():
    """The index page"""
    return render_template('index.html')
