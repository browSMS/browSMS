from twilio.rest import TwilioRestClient
from flask import session
import time


class SMSMessenger:
    def __init__(self):
       account_sid = "AC6a61c51190962188aaeb0b09d41a5cf8" # Your Account SID from www.twilio.com/console
       auth_token  = "34e9e0e89a936ceb57b72ecda13fc5b8"  # Your Auth Token from www.twilio.com/console
       self.client = TwilioRestClient(account_sid, auth_token)
       self.phone_number = '+15097693503'

    def send_message(self, body, to, media_url=[]):
    	time_since = 0
    	if session.get(str(to) + '_phone') != None:
    		time_since = session.get(str(to) + '_time')
    	else:
    		session[str(to) + '_phone'] = to
    		session[str(to) + '_time'] = time.time() - 31
    		session[str(to) + '_chars'] = 1600

    	chars_left = session.get(str(to) + '_chars')

		if time.time() - time_since <= 30 and chars_left = 0:
			# 31 just in case of rounding errors
			time.sleep(31 - elapsed)

		session[str(to) + '_time'] = time.time()
		if (len(body) > chars_left):
			session[str(to) + '_chars'] = 0			
			message = self.client.messages.create(body=body[:chars_left], to=to, from_=self.phone_number, media_url=media_url)
			send_message(self, body[chars_left:], to, media_url)
		else:
			session[str(to) + '_chars'] = chars_left - body
		

    	
'''
menu_length = 0

        for content, link in message[1]:
            menu_length += len(content)

        # Cap is 1600 chars
        length_allowed = 1600 - menu_length - 20 # 20 is the length of the string "[Current Page Content]"



        # Subtract chars needed for 0) , 1) ,...
        for num in range(1, len(message[1])):
           length_allowed - (2 + math.ceil(math.log(num, 10)))

        re.sub(r'[^\x00-\x7F]+', '', message[0])
'''


#s = SMSMessenger("+15097693503")
#s.send_message("hi", "+15093395404")
