from Scraper import scraper 
from Messenger import SMSMessenger
from flask import request, redirect, session
from app import app

messenger = SMSMessenger.SMSMessenger()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.values.get('Body')[:4] == 'http':
        url = request.values.get('Body')
        message = navigate(url)
    else:
        if request.values.get('From') in session:
            url = session[request.values.get('From')]
            options = session[url] 
            str_options = valid_options(options)
            if not request.values.get('Body') in str_options:
                message = 'Please enter a valid option:\n'
                message += make_options(options)
            else:
                if request.values.get('Body') == '0':
                    message = options[0]
                else:
                    url = options[1][int(request.values.get('Body')) - 1][1]
                    message = navigate(url)
        else:
            message = 'Please enter a valid url'
    messenger.send_message(body=message, to=request.values.get('From'))
    return 'Hey' 

def valid_options(options):
    for i in xrange(0, len(options) + 1):
        yield str(i)

def get_url(url):
    session[request.values.get('From')] = url
    out = scraper.navigate(url) 
    session[url] = scraper.navigate(url)

def make_options(options):
    message = '0) [Current Page Content]\n'
    for i, option in enumerate(options):
        message += str(i + 1) + ')  ' + option[0] + '\n'
    return message

def navigate(url):
    message = ''
    get_url(url)
    if type(session[url]) is int:
       print session[url]
       return 'Error accessing: ' + url
    message = 'You are now at: ' + url + '\n'
    message += make_options(session[url][1])
    return message
