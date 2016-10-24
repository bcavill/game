class Material(object):
    def __init__(self, name='Material', damage=0, value=0):
        self.name = name
        self.damage = damage
        self.value = value

materials = {
    'wood': Material('wood', 3, 10),
    'bronze': Material('bronze', 5, 16),
    'iron': Material('iron', 12, 30),
    'gold': Material('gold', 9, 80),
    'steel': Material('steel', 20, 50)
}
