
from mongoengine import connect, Document, StringField, DateTimeField, IntField, FloatField

class Temperature(Document):
    time = DateTimeField(required=True)
    temperatureCategory = IntField(required=True)
    Temperature = FloatField(required=True)