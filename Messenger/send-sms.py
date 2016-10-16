from twilio.rest import TwilioRestClient

account_sid = "AC6a61c51190962188aaeb0b09d41a5cf8" # Your Account SID from www.twilio.com/console
auth_token  = "34e9e0e89a936ceb57b72ecda13fc5b8"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+15093395404",    # Replace with your phone number
    from_="+15097693503") # Replace with your Twilio number


print(message.sid)
