#basic item
class Item:
    def __init__(self, name, description):
        self.name= name
        self.description = description
        pass

#equip item
class EquipItem(Item):
    def __init__(self, name, description, Type, Value):
        super().__init__(name, description)
        self.Type = Type
        self.Value = Value
        pass

#pocket item
class PocketSimpleObjectItem(Item):
    def __init__(self, name, description, Effect):
        super().__init__(name, description)
        self.Effect = Effect
        pass

    def use_effect(self, On):
        self.Effect(On)

#skill item
class SkillItem(Item):
    def __init__(self, name, description, Effect):
        super().__init__(name, description)
        self.Effect = Effect
        pass

