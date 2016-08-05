import global_vars

def exit():
    raise SystemExit

def combat():
    turn = 0
    global_vars.in_combat = True
    while global_vars.in_combat:

        if turn == 0:
            while True:
                choice = raw_input('What should you do? (attack or use item)')
                choice = choice.strip()
                if choice == 'attack':
                    if not global_vars.char.target:
                        global_vars.char.find_target()
                    global_vars.char.attack()
                    turn = 1
                    break
                elif choice == 'use item':
                    global_vars.char.use_item()
                else:
                    print "That is not a valid option try again."
        else:
           global_vars.char.target.attack()
           turn=0

"""def spawn_enemy(enemy, number=1):
    for in range(number):
        global_vars.enemies.append(enemy)
"""
