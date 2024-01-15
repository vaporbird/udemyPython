from twilio.rest import Client

account_sid = 'AC105e52fdd6126936d0325df5ed1a8a90'
auth_token = '4a7d90235b560f87be581746e24ac149'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18508015410',
  body='yoyo',

  to='+359889554867'
)

print(message.status)
