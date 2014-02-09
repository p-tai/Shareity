import sendgrid

sg = sendgrid.SendGridClient('javatai', 'Shareity')
Sharity = "javatai@gmail.com"

def sendMail(user,body):
    message = sendgrid.Mail()
    message.add_to(user)
    message.add_bcc(Sharity)
    message.set_subject("Payment Succeeded")
    message.set_html("<html><body>"+body+"</body></html>")
    message.set_text(body)
    message.set_from(Sharity)
    print(sg.send(message))

def sendPayment(to,user,payment):
    message = sendgrid.Mail()
    message.add_to(to)
    message.add_to("<cash@square.com>")
    message.add_bcc(Sharity)
    message.set_subject("$"+payment)
    message.set_text("Payment: $"+payment)
    message.set_from(user)
    print(sg.send(message))

def testMail():
    message = sendgrid.Mail()
    message.add_to('John Doe <john@email.com>')
    message.set_subject('Example')
    message.set_html('Body?')
    message.set_text('Body?')
    message.set_from('Doe John <doe@email.com>')
    sg.send(message)    

def makeBody(item,url,creator,charity,pay1,pay2):
    body = "Purchase of "+item+" succeeded.\n $"+pay1+" has been sent to "+creator+".\n $"+pay2+" has been sent to "+charity+".\n\nYour purchase can be found at "+url+""
    return body


