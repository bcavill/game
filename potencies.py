class Potency(object):

    def __init__(self, name, hp, value):
        self.name = name
        self.hp = hp
        self.value = value
        
potencies = {
    'weak': Potency('weak', 15, 20),
    'mild': Potency('mild', 40, 75),
    'potent': Potency('potent', 100, 150),
    'strong': Potency('strong', 200, 280)
}
