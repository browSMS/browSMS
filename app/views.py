from Scraper import scraper 
from Messenger import SMSMessenger
from flask import request, redirect, session
from app import app

messenger = SMSMessenger.SMSMessenger()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    body = request.values.get('Body').lower()
    sender = request.values.get('From')
    if body[0] != ':':
        if body[:4] != 'http':
            body = 'http://' + body
        url = body
        message = navigate(sender, url)
    else:
        body = body[1:]
        if sender in session:
            url = session[sender]
            options = session[url] 
            str_options = valid_options(options)
            if not body in str_options:
                message = 'Please enter a valid option:\n'
                message += make_options(options)
            else:
                if body == '0':
                    message = options[0]
                else:
                    url = options[1][int(body) - 1][1]
                    message = navigate(sender, url)
        else:
            message = 'Please enter a valid url'
    messenger.send_message(body=message, to=sender)
    return 'Hey' 

def valid_options(options):
    for i in xrange(0, len(options) + 1):
        yield str(i)

def get_url(sender, url):
    session[sender] = url
    out = scraper.navigate(url) 
    session[url] = scraper.navigate(url)

def make_options(options):
    message = ':0 [Current Page Content]\n'
    for i, option in enumerate(options):
        message += ': ' + str(i + 1) + '  ' + option[0] + '\n'
    return message

def navigate(sender, url):
    message = ''
    get_url(sender, url)
    if type(session[url]) is int:
       print session[url]
       return 'Error accessing: ' + url
    message = 'You are now at: ' + url + '\n'
    message += make_options(session[url][1])
    return message
