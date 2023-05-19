import pika

from models import User


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='sms_queue', durable=True)
print('Waiting for messages (SMS)')


def send_sms(contact):
    print(f"Send message to: {contact.phone_number}")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = User.objects.get(id=contact_id)
    send_sms(contact)
    contact.is_sms_sent = True
    contact.save()
    print(
        f"SMS sent for contact: {contact.full_name} ({contact.phone_number})")


channel.basic_consume(queue='sms_queue', on_message_callback=callback,
                      auto_ack=True)


channel.start_consuming()
