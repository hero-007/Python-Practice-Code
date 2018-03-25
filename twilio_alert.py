from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1c0264663600ecec1e50f26d6d06947d"
# Your Auth Token from twilio.com/console
auth_token  = "e69751bde5db68b99a2f9f4530621db6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918449689598", 
    from_="+16193040123"
    body="Hello from Python!")

print(message.sid)
