class DatabaseTemplate:
        
    def create(self,DB,element):
        self.createHelper(DB, element)

    def read(self,DB,element, index):
        return self.readHelper(DB,index)

    def update(self,DB, element):
        self.updateHelper(DB,element)

    def delete(self,DB,element):
        self.deleteHelper(DB,element)

    def count(self,DB,element):
        return self.countHelper(DB,element)