from mongoengine import connect, Document, StringField

class queueOperation(Document):
    operation = StringField(Required=True)