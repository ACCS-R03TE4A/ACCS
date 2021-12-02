from mongoengine import connect, Document, StringField, IntField, BinaryField

class queueOperation(Document):
    appliance = StringField(Required=True)
    protocol = IntField(Required=True)
    data = BinaryField(Required=True)
    size = IntField(Required=True)
    frequency = IntField(Required=False)


    meta = {'collection':'queueOperation'}