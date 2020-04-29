from twilio.rest import Client

account_sid = 'AC050ba09d208a81f024c197b521da1e37'
auth_token = '9dfbf2a467c3869f5f785acb0140ff39'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18452500970',
    body='I CANT BELIEVE THIS WORKS',
    to='+79516588817'
)

print(message.sid)
