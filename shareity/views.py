from shareity import app
from flask import render_template, request

#from flask.ext.pymongo import PyMongo
#from pymongo import MongoClient

import helpers, string, random, urllib, urllib2, json


#client = MongoClient('mongodb://admin:4dm1n@widmore.mongohq.com:10010/Shareity')
#client = client.Shareity

charities = {}
users = {}

venmoapi = [""]*5
venmoapi[0] = "https://sandbox-api.venmo.com/v1/payments/4?access_token=?145434160922624933?user_id="
venmoapi[1] = "venmo@venmo.com"
venmoapi[2] = "&amount="
venmoapi[3] = ""
venmoapi[4] = "&note=Donation"

charities["malarianomore"] = "Malaria No More"

pages = {}
pages["createContent"] = "screen-1e2fd0b7fb.html"
pages["addSuccess"] = "screen-6bd0bbbb97.html"
pages["makePayment"] = "screen-74dbcb1fe3.html"
pages["home"] = "screen-b34f60abef.html"
pages["about"] =  "screen-ed5c332932.html"
pages["manageContent"] = "manageContent.html"
pages["paymentAdded"] = "paymentAdded.html"

def random_string():
    length = 12
    rv = ""
    for i in range(length):
        rv+= random.choice(string.ascii_letters)
    return rv

def listUsers():
    for user in users:
        print(user)

#debug - print out all the users and all the content ids + tags
def debug():
    for email in users:
        print(email)
        for ID in users[email]:
            print(ID)
            print(users[email][ID])

def listCharities():
    for charity in charities:
        print(charity)

def sendPayment(user, amount):
    #venmoapi[1] = user
    venmoapi[3] = ("%2.f" %amount)
    print(''.join(venmoapi))
    response = urllib2.urlopen(''.join(venmoapi))
    return json.load(response)

@app.route('/content/<tag>')
def findContent(tag):
    for email in users:
        if tag in users[email]:
            return render_template(pages['makePayment'],
            name=users[email][tag][1], 
            owner=email,
            charity=charities["malarianomore"],
            tag=tag)
        print(email)
        print(tag)
    return render_template(pages['home'])

@app.route('/content/purchase/<tag>', methods=["POST"])
def purchase(tag):
    try:
        tocreator = float(request.form['creator'])
        tocharity = float(request.form['charity'])
    except ValueError:
        return render_template(pages['home'])
    
    print(tocreator)
    print(tocharity)
    
    for email in users:
        if tag in users[email]:
            
            #sendPayment(email,tocreator)
            #sendPayment(charities["malarianomore"],tocharity)
            
            return render_template(pages['paymentAdded'],
            name=users[email][tag][1], 
            owner=email,
            charity=charities["malarianomore"],
            url=users[email][tag][0],
            tocreator=tocreator,
            tocharity=tocharity)

@app.route('/manageContent')
def manageContent():
    #debug()
    return render_template(pages['manageContent'], users=users)

@app.route('/createContent')
def createContent():
    return render_template(pages['createContent'])
    
@app.route('/createContent', methods=['POST'])
def createContentPOST(ID=""):
    email = request.form['email'].lower()
    contentid = request.form['url'].lower()
    name = request.form['name']
    #check if the user has added content before.
    if email not in users:
        #If not, create a new user.
        users[email] = {}
    
    #search to see if the content url was already added
    for ID in users[email]:
        if contentid in users[email][ID]:
            return render_template(pages['addSuccess'],ID=ID)
    
    #create a random tag for the contentid
    ID = random_string()
    users[email][ID] = [contentid, name]
    
    return render_template(pages['addSuccess'],ID=ID)

#@app.route('/charities')

@app.route('/home')
@app.route('/')
def index():
    """The index page"""
    return render_template(pages['home'])
