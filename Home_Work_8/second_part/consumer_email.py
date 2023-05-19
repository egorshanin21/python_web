import pika
from mongoengine import connect
import connect as conn
from models import User

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)

print('Waiting for messages (Email)')


def send_email(contact):
    print(f"Send email to: {contact.email}")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = User.objects.get(id=contact_id)
    send_email(contact)
    contact.is_email_sent = True
    contact.save()
    print(f"Email sent for contact: {contact.full_name} ({contact.email})")


channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)


channel.start_consuming()