from mongoengine import Document, StringField, DateField, ReferenceField, \
    ListField, connect


connect(host="mongodb+srv://egorshanin21:968231@cluster0.i6q0c1p."
             "mongodb.net/test2", ssl=True)


class Author(Document):
    fullname = StringField(required=True)
    born_date = DateField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(required=True)
    quote = StringField(required=True)
    author = ReferenceField(Author)
