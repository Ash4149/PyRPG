import event_package

class EventPos:
    def __init__(self, code, position, map):
        self.position = position
        self.code = code
        self.map = map
        pass

    def verify(self, object, map):
        if self.map == map and object.x == self.position[0] and object.y == self.position[1]:
            return True