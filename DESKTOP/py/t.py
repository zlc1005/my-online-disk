from twilio.rest import Client

account_sid = 'AC5f48d61a84557ac0f13f0157003ecb33'
auth_token = 'd328592b72cac96583498a0de6837476'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hello!",
                     from_='+17164543790',
                     to='+17783162618'
                 )
print(message.status)