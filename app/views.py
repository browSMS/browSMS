import Scraper
from Messenger import SMSMessenger
from flask import request, redirect, session
from app import app
#import twilio.twiml

messenger = SMSMessenger()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.get('body')[:4] == 'http':
        url = request.get('body')
        message = navigate(url)
    else:
    	if request.get('To') in session:
    	    url = session[request.get('To')]
            options = session[url] 
            str_options = valid_options(options)
            if not request.get('body') in str_options:
                message = 'Please enter a valid option:\n'
                message += make_options(options)
            else:
                url = options[int(request.get('body'))][1]
                message = navigate(url)
	else:
            message = 'Please enter a valid url'
    messenger.send_message(body=message, to=request.get('From'))
    return 'Hey' 

def valid_options(options):
    for i in xrange(len(options)):
        yield str(i)

def get_url(url):
    session[request.get('To')] = url
    session[url] = Scraper.navigate(url)

def add_extra_options(options):
    pass
     
def make_options(options):
    message = ''
    for i, options in options:
        message += str(i) + ')  ' + option[0] + '\n'
    return message

def navigate(url):
    message = ''
    get_url(url, session)
    message = 'You are now at: ' + url 
    message += make_options(session[url])
    return message

