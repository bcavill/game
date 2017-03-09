import items
import random
import spells

names = ['Kolanji', 'Zakaro', 'Tumadi', 'Rikako', 'Jinmalan', 'Ichako', 'Dorizin', 'Makrokin', 'Kinjabal', 'Venkoa', 'Dazro', 'Limdaka', 'Jumanji', 'Ouji']

def rand_name():
	i = random.randint(0, len(names) - 1)
        return names[i]

class character():

    def __init__(self, Game):
        self.Game = Game
        self.hp = 0 + 10 * 0
        self.name = None
        self.level = level
        self.defense = 0 * self.level
        self.damage = 0 * self.level
        self.target = None
        self.weapon = None
        
    def attack(self):
        print '%s %s attacked %s %s' % (self.__class__.__name__, self.name, self.target.__class__.__name__, self.target.name)

        if self.weapon != None:
            dmg = self.damage + self.weapon.damage
        else:
            dmg = self.damage
        
        self.target.attacked(dmg, self)

    def attacked(self, wound, attacker):
        if self.target == None:
            self.target=attacker

        hit_chance = random.random()

        if hit_chance <= 0.2:
            print '%s %ss\' attack missed \n' % (attacker.__class__.__name__, attacker.name)
            return

        wound = wound - float(self.defense) / 100 * random.randint(30, 60)
        self.hp = self.hp - wound
        print '%s %s took %s points of damage from %s %s' % (self.__class__.__name__, self.name, wound, attacker.__class__.__name__, attacker.name)

        self.is_dead(attacker)

    def is_dead(self, attacker):
        if self.hp <= 0:
            print '%s has been defeated. %s is victorious!' % (self.name, attacker.name)
            del self.Game.enemies[len(self.Game.enemies) - 1]
            attacker.victory(self.level)
            attacker.target = None
            self.Game.in_combat = False
        else:
            print '%s %s\'s hp fell to %s\n' % (self.__class__.__name__, self.name, self.hp)

class player(character):

    def __init__(self, Game):
        self.Game = Game
        self.level = 1
        self.max_hp = 100 + 10 * self.level
        self.hp = self.max_hp
        self.name = None
        self.defense = 10 * self.level
        self.damage = 10 * self.level
        self.target = None
        self.inventory = [items.health('potion', 'weak')]
        self.spells = [spells.fireball('fireball')]
        self.xp = 0
        self.gold = 50
        self.weapon = items.weapon('dagger', 'bronze')

    def victory(self, level):
        xp_gained = level * 20 + random.randint(10, 50)
        gold_gained = level * random.randint(10, 50)
        self.xp = self.xp + xp_gained
        self.gold = self.gold + gold_gained
        self.hp = self.max_hp

        print "%s %s gained %s xp and recovered %s gold" % (self.__class__.__name__, self.name, xp_gained, gold_gained)

        if self.xp >= self.level * 100:
            self.level_up()

    def is_dead(self, attacker):
        if self.hp <= 0:
            print '%s has been defeated. %s is victorious!' % (self.name, attacker.name)
            print 'GAME OVER'
            self.Game.exit()
        else:
            print '%s %s\'s hp fell to %s\n' % (self.__class__.__name__, self.name, self.hp)

    def level_up(self):
        self.xp = 0
        self.level = self.level + 1
        self.hp = 100 + 10 * self.level
        self.defense = 10 * self.level
        self.damage = 10 * self.level
        print '%s %s has reached level %s!' % (self.__class__.__name__, self.name, self.level)

    def use_item(self):
        while True:
            items = ['none']
            for thing in self.inventory:
                items.append('{} {}'.format(thing.strength.name, thing.name))
            item = raw_input('You have {} in your inventory. Which item would you like to use? '.format(items))
            item = self.Game.sanitize(item)
            
            if item == 'none':
                break
            for x, i in enumerate(self.inventory):
                if '{} {}'.format(i.strength.name, i.name) == item:
                    item = i
                    if item.useable:
                        item.use(self)
                        del self.inventory[x]
                        break
                    elif item.equipable:
                        self.inventory.append(self.weapon)
                        self.weapon = self.inventory[x]
                        del self.inventory[x]
                        break
                if x == len(self.inventory) - 1:
                    print "You don't know that spell."

    def cast_spell(self):
        while True:
            items = ['none']
            for spell in self.spells:
                items.append(spell.name)
            spell = raw_input('You have {} available to cast. Which Spell should you cast? '.format(items))
            spell = self.Game.sanitize(spell)

            if spell == 'none':
                break

            for x, i in enumerate(self.spells):
                if i.name == spell:
                    spell = i
                    self.spells[x].cast(self, self.target)
                    break
                if x == len(self.inventory) - 1:
                    print "You don't have %s in your inventory" % item

    def find_target(self):
        enemy_count = len(self.Game.enemies)
        if enemy_count == 0:
            self.Game.in_combat = False
            return False

        self.target = self.Game.enemies[enemy_count - 1]
        self.Game.in_combat = True
        print 'Now attacking {} {}'.format(self.target.__class__.__name__, self.target.name)
        return True

class trol(character):

    def __init__(self, Game):
        self.Game = Game
        self.level = Game.char.level
	self.hp = 120 + 10 * self.level
        self.name = rand_name()
        self.defense = 5 * self.level
        self.damage = 6  * self.level
        self.target = None
        self.weapon = items.weapon('club', 'wood')

class ghast(character):

    def __init__(self, Game):
        self.name = 'Fred'
        self.Game = Game
        self.level = Game.char.level
        self.hp = 70 + 10 * self.level
        self.name = rand_name()
        self.defense = 12 * self.level
        self.damage = 12  * self.level
        self.target = None
        self.weapon = None

class merchant():

    def __init__(self, Game):
        self.Game = Game
        self.maxgold = 500
        self.gold = 500
        self.inventory = []

    def generate_stock(self):
        self.gold = self.maxgold
        for i in range(random.randrange(5, 15)):
            item = random.randint(0, 1)
            if item == 0:
                weapon = random.choice(items.weapons.keys())
                material = random.choice(items.materials.keys())
                self.inventory.append(items.weapon(weapon, material))
            elif item == 1:
                self.inventory.append(items.health('potion', random.choice(items.potencies.keys())))

    def barter(self):
        while True:
            print 'You have {} gold'.format(self.Game.char.gold)
            print 'The merchant has {} gold'.format(self.gold)
            action = raw_input('How can I help you today? [\'none\', \'buy\', \'sell\'] ')
            action = self.Game.sanitize(action)
            if action == 'none':
                break
            elif action == 'buy' or action == 'sell':
                if action == 'buy':
                    inv = self.inventory
                    question = 'The following items are available to buy: {} Which item would you like to buy? '
                    args = (self, self.Game.char)
                    confirm_msg = 'You bought {} for {} gold'
                    error_msg = 'You don\'t have enough gold to buy {} '
                else:
                    inv = self.Game.char.inventory
                    question = 'You have the following items available to sell: {} Which item would you like to sell? '
                    args = (self.Game.char, self)
                    confirm_msg = 'You sold {} for {} gold'
                    error_msg = 'The merchant can\'t to buy {} '

                items = ['none']
                for thing in inv:
                    items.append('{} {}'.format(thing.strength.name, thing.name))
                    items.append(thing.value)
                item = raw_input(question.format(items))
                for x, i in enumerate(inv):
                    thing = '{} {}'.format(i.strength.name, i.name)
                    if thing == item:
                        i.sell(args[0], args[1])
                        print confirm_msg.format(thing, i.value)
                        break

                    if x == len(inv) - 1:
                        print error_msg.format(item)
