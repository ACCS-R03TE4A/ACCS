from mongoengine import connect, Document, StringField, IntField, BinaryField,ObjectIdField

class queueOperation(Document):
    appliance = StringField(Required=True)
    protocol = IntField(Required=True)
    data = BinaryField(Required=True)
    size = IntField(Required=True)
    frequency = IntField(Required=False)


    meta = {'collection':'queueOperation'}

    def __str__(self):
        return f"{self.appliance}, {self.protocol}, {self.data}, {self.size}"
    

    
    def get_dict(self):

        ope_dict = {"appliance":self.appliance, 
        "protocol":self.protocol, "data":int(self.data), 
        "size":self.size}

        return ope_dict