from flask import request, redirect, session
from app import app
import twilio.twiml

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    resp = twilio.twiml.Response()
    if request.get('body')[:4] == 'http':
        url = request.get('body')
        session
    else:
    	if request.get('To') in session:
    	    url = session[request.get('To')]
            options = session[session[url]] 
            str_options = valid_options(options)
            if not request.get('body') in str_options:
                message = 'Please enter a valid option:\n'
                for i, options in options:
                    message += str(i) + ')  ' + option + '\n'
            else:
                options[int(request.get('body'))](session)
	else:
    return str(resp)

def valid_options(options):
    for i in xrange(len(options)):
        yield str(i)

def get_url(to, url):
    def navigate(session):
        session[to] = url
        options = Scraper.navigate(to, url)
        session[url] = Scraper.navigate(to, url)
    return navigate 

     
