from app import app, request
import twilio.twiml

@app.route('/')
@app.route('/index')
def index():
    resp = twilio.twiml.Response()
    resp.message(request.data)
