from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER
import time

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number, message):
    try:
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=to_number
        )
        print(f"Mensaje de WhatsApp enviado correctamente a {to_number}. SID: {message.sid}")
    except Exception as e:
        print(f"No se pudo enviar el mensaje de WhatsApp: {e}")

while 0 < 1:
    time.sleep(1)
    send_whatsapp_message('whatsapp:+34692682368', 'Rayos y centellas!')
