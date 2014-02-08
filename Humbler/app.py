from flask import Flask, render_template, request
app = Flask(__name__)
charities = {}
content = {}

@app.route('/?content')

def listContent():
    return content


@app.route('/?charities')

def listCharities():
    return charity


@app.route('/')

def home():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run('0.0.0.0' , debug=True)
