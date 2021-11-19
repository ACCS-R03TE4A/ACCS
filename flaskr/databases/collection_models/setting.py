from mongoengine import connect, Document, StringField

class Setting(Document):
    postnumber = StringField(Required=True)