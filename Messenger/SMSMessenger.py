from twilio.rest import TwilioRestClient

class SMSMessenger:
    def __init__(self):
       account_sid = "AC6a61c51190962188aaeb0b09d41a5cf8" # Your Account SID from www.twilio.com/console
       auth_token  = "34e9e0e89a936ceb57b72ecda13fc5b8"  # Your Auth Token from www.twilio.com/console
       self.client = TwilioRestClient(account_sid, auth_token)
       self.phone_number = '+15097693503'

    def send_message(self, body, to, media_url=[]):
        message = self.client.messages.create(body=body, to=to, from_=self.phone_number, media_url=media_url) 
