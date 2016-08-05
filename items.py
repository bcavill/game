from materials import *
from potencies import *

class item():

    def __init__(self):
        self.value = 0
        self.equipable = False
        self.useable = False

    def sell(self, seller, buyer):
        seller.gold = seller.gold + self.value
        buyer.gold = buyer.gold - self.value
        seller.inventory.remove(self)
        buyer.inventory.append(self)
        print "%s %s purchased %s from %s %s for %s gold." % (seller.__class__.__name__, seller.name, self.__class__.__name__, buyer.__class__.__name__, buyer.name, self.value)

class weapon(item):

    def __init__(self, material):
        self.material = materials[material]
        self.damage = 0 + self.material.damage
        self.value = 0 + self.material.value
        self.equipable = True
        self.useable = False
        
class dagger(weapon):

    def __init__(self, material):
        self.material = materials[material]
        self.damage = 5 + self.material.damage
        self.value = 5 + self.material.value
        self.equipable = True
        self.useable = False
        
class sword(weapon):

    def __init__(self, material):
        self.material = materials[material]
        self.damage = 12 + self.material.damage
        self.value = 12 + self.material.value
        self.equipable = True
        self.useable = False

class club(weapon):

    def __init__(self, material):
        self.material = materials[material]
        self.damage = 9 + self.material.damage
        self.value = 9 + self.material.value
        self.equipable = True
        self.useable = False

class potion(item):

    def __init__(self, potency):
        self.potency = potencies[potency]
        self.hp = 20 + self.potency.hp
        self.value = 25 + self.potency.value
        self.equipable = False
        self.useable = True
        
    def use(self, target):
        target.hp = target.hp + self.hp
        print "%s %s used %s and healed %s points of health" % (target.__class__.__name__, target.name, self.__class__.__name__, self.hp)
