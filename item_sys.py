#basic item
class Item:
    def __init__(self, name, description):
        self.name= name
        self.description = description
        pass

    def __eq__(self, name):
        return self.name == name
        pass

    def __hash__(self):
        return hash(self.name)
        pass