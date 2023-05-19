import pika

from datetime import datetime

from faker import Faker
import json

from models import User

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()


fake = Faker()


def main():
    for _ in range(10):
        full_name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        user = User(full_name=full_name, email=email,
                          phone_number=phone_number)
        user.save()

        channel.basic_publish(
            exchange='',
            routing_key='sms_queue',
            body=str(user.id).encode(),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=str(user.id).encode(),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        print(
            f"sent for contact: {user.full_name} ({user.phone_number})")
        print(f"sent for contact: {user.full_name} ({user.email})")
    print("The producer.py script is complete.")
    connection.close()


if __name__ == '__main__':
    main()
