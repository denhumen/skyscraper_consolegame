"""
Main module for
the game
"""
from classes import Building, Player, Inventory, Item

if __name__ == "__main__":
    print("  __  __ __ _  _  __    ___ ____   ___  ____   ____ ____ ")
    print(" (( \ || // \\// (( \  //   || \\ // \\ || \\ ||    || \\")
    print("  \\  ||<<   )/   \\  ((    ||_// ||=|| ||_// ||==  ||_//")
    print(" \_)) || \\ //   \_))  \\__ || \\ || || ||    ||___ || \\\n")
    print("Hi player, you was locked by anonimus person in unknown building")
    print("The game will be ended when you kill 2 enemies or become dead")
    first_item = Item("Kitchen Knife", 10)
    building = Building(5)
    building.create()
    player = Player()
    inventory = Inventory()
    inventory.add_item(first_item)
    enemy_counter = 0
    happy = False
    while True:
        building.show_map()
        print("Enter side where you want to go")
        side = input("Enter w, a, s or d: ")
        if side == "w":
            state = building.move_up()
            if not state:
                continue
        elif side == "s":
            state = building.move_down()
            if not state:
                continue
        elif side == "a":
            state = building.move_left()
            if not state:
                continue
        elif side == "d":
            state = building.move_right()
            if not state:
                continue
        else:
            print("\nWrong input\n")
            continue
        print("\nNew Location:")
        building.show_map()
        room = building.get_current_room_information()
        room.show_information()
        end = room.room_action(inventory, player)
        if end == False:
            break
        if room.enemy != None:
            enemy_counter += 1
        if enemy_counter >= 2:
            happy = True
            break
        if player.health <= 0:
            break
    if happy:
        player.happy_end()
    else:
        player.unhappy_end()