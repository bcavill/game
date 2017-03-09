from potencies import *
from materials import *

class spell(object):

    def __init__(self, name):
        self.name = name
        self.damage = 20
        self.element = None

    def cast(self, caster, target):
        print(" {0} cast {1} at {2}").format(caster.name, self.name, target.name)
        target.attacked(self.damage, caster)

class fireball(object):

    def __init__(self, name):
        self.name = name
        self.damage = 20
        self.element = 'fire'

    def cast(self, caster, target):
        print(" {0} cast {1} at {2}").format(caster.name, self.name, target.name)
        target.attacked(self.damage, caster)
