from humbler import app
from flask import render_template, request
import helpers, string, random

charities = {}
users = {}

pages = {}
pages["createContent"] = "screen-1e2fd0b7fb.html"
pages["addSuccess"] = "screen-6bd0bbbb97.html"
pages["makePayment"] = "screen-74dbcb1fe3.html"
pages["home"] = "screen-b34f60abef.html"
pages["about"] =  "screen-ed5c332932.html"

def random_string():
    length = 12
    rv = ""
    for i in range(length):
        rv+= random.choice(string.ascii_letters)
    return rv

def listUsers():
    for user in users:
        print(user)
        
def listContent():
    for item in content:
        print(item)

def listCharities():
    for charity in charities:
        print(charity)


@app.route('/createContent')
def createContent():
    return render_template(pages['createContent'])
    
@app.route('/createContent', methods=['POST'])
def addContent():
    email = request.form['email'].lower()
    contentid = request.form['url'].lower()
    
    #check if the user has added content before.
    if email not in users:
        #If not, create a new user.
        users[email] = {}
    
    #search to see if the content url was already added
    if contentid in users[email]:
        return render_template(pages['addSuccess'], content=users[email][contentid])
    
    #create a random tag for the contentid
    users[email][contentid] = random_string()

    #debug - print out all the users and all the content ids + tags
    for email in users:
        print(email)
        for ID in users[email]:
            print(ID)
            print(users[email][ID])
    
    return render_template(pages['addSuccess'], content=users[email][contentid])

#@app.route('/manageContent')

#@app.route('/charities')

@app.route('/home')
@app.route('/')
def index():
    """The index page"""
    return render_template(pages['home'])
