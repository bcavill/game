from items import *
import global_vars
import functions
import random

class character():

    def __init__(self, name, level):
        self.hp = 0 + 10 * level
        self.name = name
        self.level = level
        self.defense = 0 * level
        self.damage = 0  * level
        self.target = None
        self.weapon = None
        
    def attack(self):
        hit_chance = random.random()
        
        print '%s %s attacked %s %s' % (self.__class__.__name__, self.name, self.target.__class__.__name__, self.target.name)
        
        if hit_chance <= 0.2:
            print '%s %ss\' attack missed \n' % (self.__class__.__name__, self.name)
            return
        
        self.target.attacked(self.damage + self.weapon.damage, self)

    def attacked(self, wound, attacker):
        wound = wound - float(self.defense) / 100 * random.randint(30, 60)
        self.hp = self.hp - wound
        print '%s %s took %s points of damage from %s %s' % (self.__class__.__name__, self.name, wound, attacker.__class__.__name__, attacker.name)
        
        if self.target == None:
            self.target=attacker
        self.is_dead(attacker)

    def is_dead(self, attacker):
        if self.hp <= 0:
            print '%s has been defeated. %s is victorious!' % (self.name, attacker.name)
            if str(self.__class__.__name__) == 'player':
                print 'GAME OVER'
                exit()
            else:
                del global_vars.enemies[len(global_vars.enemies) - 1]
                attacker.victory(self.level)
                attacker.find_target()
        else:
            print '%s %s\'s hp fell to %s\n' % (self.__class__.__name__, self.name, self.hp)
        
class player(character):

    def __init__(self, name):
        self.level = 1
        self.max_hp = 100 + 10 * self.level
        self.hp = self.max_hp
        self.name = name
        self.defense = 10 * self.level
        self.damage = 10 * self.level
        self.target = None
        self.inventory = [dagger('bronze'), potion('weak')]
        self.xp = 0
        self.gold = 50
        self.weapon = self.inventory[0]

    def victory(self, level):
        xp_gained = level * 20 + random.randint(10, 50)
        gold_gained = level * random.randint(1, 50)
        self.xp = self.xp + xp_gained
        self.gold = self.gold + gold_gained
        self.hp = self.max_hp

        print "%s %s gained %s xp and recovered %s gold" % (self.__class__.__name__, self.name, xp_gained, gold_gained)

        if self.xp >= self.level * 100:
            self.level_up()

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
                items.append(thing.__class__.__name__)
            item = raw_input('You have %s in your inventory. Which item would you like to use? ' % items)
            if item == 'none':
                break
            for x, i in enumerate(self.inventory):
                if i.__class__.__name__ == item:
                    item = i
                
                    if item.useable:
                        item.use(self)
                        del self.inventory[x]
                        break
                    print "You can't use your %s." % item.__class__.__name__
                    break
                if x == len(self.inventory) - 1:
                    print "You don't have %s in your inventory" % item

    def find_target(self):
        enemy_count = len(global_vars.enemies)
        if enemy_count == 0:
            global_vars.in_combat = False
            return False

        self.target = global_vars.enemies[enemy_count - 1]
        return True

class trol(character):

    def __init__(self, name, level):
        self.hp = 120 + 10 * level
        self.name = name
        self.level = level
        self.defense = 5 * level
        self.damage = 6  * level
        self.target = None
        self.weapon = club('wood')

class ghast(character):

    def __init__(self, name, level):
        self.hp = 70 + 10 * level
        self.name = name
        self.level = level
        self.defense = 12 * level
        self.damage = 12  * level
        self.target = None
        self.weapon = None
