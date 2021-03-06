import characters

class game():

    def __init__(self):
        self.char = characters.player(self)
        self.enemies = []
        self.species = [characters.trol(self), characters.ghast(self)]
        self.merchant = characters.merchant(self)
        self.in_combat = False

    def new_game(self):
        name = raw_input('What is thy name brave warrior? ')
        self.char.name = name

        print('Greetings %s, a trol is attacking our village please help us.') % self.char.name
        self.spawn_enemy(characters.trol(self), 1)
        self.char.find_target()

        while True:
            self.loop()

    def exit(self):
        raise SystemExit

    def loop(self):
        if self.in_combat:
            turn = 0
            while self.in_combat:

                if turn == 0:
                    while True:
                        choice = raw_input('What should you do? [\'Attack\', \'Use an item\', \'Cast a spell\'] ')
                        choice = self.sanitize(choice)

                        if choice == 'attack':
                            self.char.attack()
                            turn = 1
                            break
                        elif choice == 'use an item':
                            self.char.use_item()
                        elif choice == 'cast a spell':
                            self.char.cast_spell()
                            turn = 1
                            break
                        else:
                            print "That is not a valid option try again."
                else:
                    self.char.target.attack()
                    turn=0
        else:
            while True:
                choice = raw_input('What would you like to do? [\'Quit\', \'Visit the store\', \'Go hunting\'] ')
                choice = self.sanitize(choice)

                if choice == 'visit the store':
                    self.merchant.generate_stock()
                    self.merchant.barter()
                elif choice == 'go hunting':
                    self.spawn_enemy()
                    self.char.find_target()
                    break
                elif choice == 'quit':
                    self.exit()

    def spawn_enemy(self, enemy=None, number=1):
        import random
        for i in range(number):
            if enemy == None:
                enemy = random.choice(self.species)
            self.enemies.append(enemy)

    def sanitize(self, choice):
        choice = choice.strip()
        choice = choice.lower()
        return choice

if __name__ == '__main__':
    Game = game()
    Game.new_game()
