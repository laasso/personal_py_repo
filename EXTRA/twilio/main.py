from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

# Create a Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to_number, message):
    try:
        # Use the Twilio client to send an SMS message
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"Message sent successfully to {to_number} with SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Example usage:
# Replace 'desired_number' with the desired recipient's phone number
# Replace 'desired_message' with the desired message
send_sms('desired_number', 'desired_message')
