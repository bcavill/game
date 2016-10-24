from potencies import *
from materials import *

class item(object):

    def __init__(self, name):
        self.name = name
        self.value = 0
        self.equipable = False
        self.useable = False

    def sell(self, seller, buyer):
        if buyer.gold >= self.value:
            seller.gold = seller.gold + self.value
            buyer.gold = buyer.gold - self.value
            seller.inventory.remove(self)
            buyer.inventory.append(self)
            return True
        return False

class weapon(item):

    def __init__(self, name='dagger', material='wood'):
        weapon = weapons[name]
        self.name = name
        self.strength = materials[material]
        self.damage = weapon['damage'] + self.strength.damage
        self.value = weapon['value'] + self.strength.value
        self.equipable = True
        self.useable = False

class health(item):

    def __init__(self, name='potion', potency='weak'):
        self.name = name
        self.strength = potencies[potency]
        self.hp = 20 + self.strength.hp
        self.value = 25 + self.strength.value
        self.equipable = False
        self.useable = True

    def use(self, target):
        target.hp = target.hp + self.hp
        print "%s %s used %s %s and healed %s points of health" % (target.__class__.__name__, target.name, self.strength.name, self.name, self.hp)

weapons = {
    'dagger': {'damage': 5, 'value': 20},
    'sword': {'damage': 10, 'value': 60},
    'club': {'damage': 7, 'value': 45}
}
