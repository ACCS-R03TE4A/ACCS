from mongoengine import connect, Document, StringField, IntField, BinaryField,ObjectIdField

class queueOperation(Document):
    _id = ObjectIdField(Required=True, primary_key=True)
    appliance = StringField(Required=True)
    protocol = IntField(Required=True)
    data = BinaryField(Required=True)
    size = IntField(Required=True)
    frequency = IntField(Required=False)


    meta = {'collection':'queueOperation'}

    def __str__(self):
        return f"{self._id}, {self.appliance}, {self.protocol}, {self.data}, {self.size}"
        
        #
        # ope_list = [{self._id}, {self.appliance}, {self.protocol}, {self.data}, {self.size}]
        # return ope_list

    
    def get_dict(self):

        ope_dict = {"_id":str(self._id), "appliance":self.appliance, 
        "protocol":self.protocol, "data":int(self.data), 
        "size":self.size}

        return ope_dict