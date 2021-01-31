from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item

# Create black magic
fire = Spell("Fire", 10, 100, "black")
meteor = Spell("Thunder", 10, 100, "black")
chaos_bolt = Spell("Chaos", 10, 100, "black")
necromant = Spell("Necromant", 20, 200, "black")
corruption = Spell("Corruption", 14, 140, "black")

# Create good magic

cure = Spell("Cure", 12, 120, "white")
renew = Spell("Renew", 18, 200, "white")

# Create items - heal

potion = Item("Potion", "potion", "Heals 50 HP", 50)
greatpotion = Item("GreatPotion", "potion", "Heals 100 HP", 100)

# Create items - damage

molotov = Item("Cocktail Molotov", "bomb", "deals 500 damage", 500)

# Instantiate Player and enemy

player_spells = [fire, chaos_bolt, necromant, corruption, cure, renew]
player_items = [{"item": potion, "quantity": 5},
                {"item": greatpotion, "quantity": 3},
                {"item": molotov, "quantity": 2}]


player = Person(500, 200, 45, 35, player_spells, player_items )

enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("=========================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You Attacked for ", dmg, "points of damage.", enemy.get_hp())

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\n Not enough MP" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC + "\n")

    elif index == 2:
        player.choose_item()
        item_choice = int(input(" Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]
        player.items[item_choice]["quantity"] -= 1


        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

        elif item.type == "greatpotion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

        elif item.type == "bomb":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " takes damage", str(item.prop), "HP" + bcolors.ENDC)



    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg, "Player HP ", player.get_hp())

    print("-------------------")

    print("ENEMY HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("YOUR HP", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("YOUR MP", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU WIN" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "YOU LOSE!" + bcolors.ENDC)
        running = False
