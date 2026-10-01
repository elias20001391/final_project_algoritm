



import random


damages = [10,20,30,40,50]

magics = ["fire","water","wind","ice"]

enemy_damage = 100
your_damage = 100


while True:
    if enemy_damage <= 0:
        if enemy_damage < your_damage:
            print("you are win")
            break
    elif your_damage <= 0:
        print("you are lose")
        break
    else:
        magic_menu = input("""
enter a '1' for use fire
enter a '2' for use water
enter a '3' for use wind
enter a '4' for use ice

enter your choice:""")
        match magic_menu:
            case "1":
                fire_damages = random.choice(damages)
                fire_enemy_damage = random.choice(damages)
                enemy_damage -= fire_damages
                your_damage -= fire_enemy_damage
                print("you:",your_damage)
                print("enemy:",enemy_damage)
            case "2":
                water_damages = random.choice(damages)
                water_enemy_damage = random.choice(damages)
                enemy_damage -= water_damages
                your_damage -= water_enemy_damage
                print("you:",your_damage)
                print("enemy:",enemy_damage)
            case "3":
                fire_damages = random.choice(damages)
                fire_enemy_damage = random.choice(damages)
                enemy_damage -= fire_damages
                your_damage -= fire_enemy_damage
                print("you:",your_damage)
                print("enemy:",enemy_damage)
            case "4":
                ice_damages = random.choice(damages)
                ice_enemy_damage = random.choice(damages)
                enemy_damage -= ice_damages
                your_damage -= ice_enemy_damage
                print("you:",your_damage)
                print("enemy:",enemy_damage)
            case _:
                print("invailed")
            