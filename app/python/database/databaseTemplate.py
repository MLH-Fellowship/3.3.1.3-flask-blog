class DatabaseTemplate:
    
    def create(DB,element):
        createHelper(DB, element)

    def read(DB,element, index):
        return readHelper(DB,element,index)

    def update(DB, element):
        updateHelper(DB,element)

    def delete(DB,element):
        deleteHelper(DB,element)