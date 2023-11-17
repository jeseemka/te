import pywhatkit as kit

# Specify the phone number (including the country code) of the recipient
phone_number = '+918547452080'

# Message you want to send
message = 'Hello, this is a WhatsApp message sent from Python!'

# Specify the time at which you want to send the message (24-hour format)
hour = 3
minute = 48 # 12:00 PM

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)
