from mongoengine import Document, StringField, BooleanField, connect


connect(host="mongodb+srv://egorshanin21:968231@cluster0.i6q0c1p."
             "mongodb.net/test2", ssl=True)


class User(Document):
    full_name = StringField()
    email = StringField()
    is_email_sent = BooleanField(default=False)
    phone_number = StringField()
    is_sms_sent = BooleanField(default=False)
    delivery_method = StringField(choices=['email', 'sms'], default='email')