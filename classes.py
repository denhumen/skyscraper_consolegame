"""
Module where classes
for main.py are created
"""
import random
import os

class Player():
    """
    Player class
    """
    def __init__(self) -> None:
        self.health = 100

    def speak(self):
        """
        Speak method
        """

    def happy_end(self):
        """
        Happy end method
        """
        print("\n#######################")
        print("YOU SUCCESSFULLY KILLED 2 ENEMIES")
        print("#######################\n")

    def unhappy_end(self):
        """
        Unhappy end method
        """
        print("\n#######################")
        print("YOU DIED")
        print("#######################\n")

class Person():
    """
    Person class
    """
    def __init__(self) -> None:
        self.name = self.get_random_name()

    def get_random_name(self):
        """
        Get random name method
        """
        with open(os.path.join(os.getcwd(), 'names.csv'), 'r', encoding="utf-8") as names_file:
            names = names_file.read().splitlines()
        name_idx = random.randrange(0, len(names))
        return names[name_idx]

class Friend(Person):
    """
    Friend class
    """
    def __init__(self) -> None:
        super().__init__()
        self.type = "friend"

    def __get_random_phrase(self):
        """
        Get random phrase method
        """
        with open(os.path.join(os.getcwd(), 'phrases.csv'), 'r', encoding='utf-8') as phrases_file:
            phrases = phrases_file.read().splitlines()
        ph_idx = random.randrange(0, len(phrases))
        return phrases[ph_idx]

    def talk(self):
        """
        Talk method
        """
        phrase = self.__get_random_phrase()
        return f"\n{self.name}: {phrase}\n"

    def get_information(self):
        """
        Show information method
        """
        return f"{self.name} [{self.type}]"

class Enemy(Person):
    """
    Enemy class
    """
    def __init__(self) -> None:
        super().__init__()
        self.type = "enemy"

    def get_information(self):
        """
        Show information method
        """
        return f"{self.name} [{self.type}]"

class Item():
    """
    Item class
    """
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

    def show_info(self):
        """
        Show info method
        """
        print(f"Name: {self.name}")
        print(f"Damage: {self.damage}")
        

class Inventory():
    """
    Inventory class
    """
    def __init__(self) -> None:
        self.items = []

    def get_inventory(self):
        """
        Get function for inventory
        """
        return self.items

    def add_item(self, item: Item):
        """
        Add item class
        """
        self.items.append(item)

class Room():
    """
    Room class
    """
    def __init__(self) -> None:
        self.name = self.get_random_name()
        num = random.randrange(0, 11)
        if num < 7:
            self.friend = Friend()
            self.enemy = None
        else:
            self.friend = None
            self.enemy = Enemy()
        self.item = self.get_random_gun()

    def get_random_name(self):
        """
        Get random name method
        """
        with open(os.path.join(os.getcwd(), 'rooms.csv'), 'r', encoding='utf-8') as room_names_file:
            room_names = room_names_file.read().splitlines()
        room_name_idx = random.randrange(0, len(room_names))
        return room_names[room_name_idx]

    def get_random_gun(self):
        """
        Get random gun method
        """
        with open(os.path.join(os.getcwd(), 'guns.csv'), 'r', encoding='utf-8') as guns_file:
            guns_names = guns_file.read().splitlines()
        gun_idx = random.randrange(0, len(guns_names))
        return Item(guns_names[gun_idx], random.randrange(10, 100))

    def show_information(self):
        """
        Show information method
        """
        print(f"Current room: {self.name}")
        print('-----------------------------')
        if self.friend == None:
            print(f"Person: {self.enemy.get_information()}")
        else:
            print(f"Person: {self.friend.get_information()}")

    def room_action(self, inventory: Inventory, player: Player):
        """
        Room action method
        """
        if self.friend != None:
            print("This room doesn't contain your enemies!")
            while True:
                print(">talk")
                print(">take item")
                print(">go")
                inp = input('> ')
                if inp == "talk":
                    print(self.friend.talk())
                elif inp == "take item":
                    if self.item not in inventory.items:
                        print()
                        print("You have cliemed new item!")
                        self.item.show_info()
                        print()
                        inventory.add_item(self.item)
                    else:
                        print("There are no items here!")
                elif inp == "go":
                    break
                else:
                    print("Wrong input!")
        else:
            print("You meet one of your enemies!")
            print("Choose item from your inventory, wrong input will kill you:")
            for item in inventory.items:
                print(item.name)
            inp = input('gun name: ')
            if inp in [item.name for item in inventory.items]:
                got_dam = random.randrange(0, 101)
                player.health -= got_dam
                print(f"You got {got_dam} damage, but enemy was killed")
            else:
                return False

class Building():
    """
    Building class
    """
    __current_pos = (0, 0)

    def __init__(self, size) -> None:
        self.rooms = []
        self.size = size

    def set_current_pos(self, x: int, y: int):
        """
        Set current position method
        """
        self.__current_pos = (x, y)

    def create(self):
        """
        Create building with
        Rooms
        """
        self.rooms = [[Room() for x in range(self.size)] for _ in range(self.size)]

    def move_up(self):
        """
        Move up method
        """
        x0, y0 = self.__current_pos
        try:
            if x0-1 < 0:
                raise IndexError
            _ = self.rooms[x0-1][y0]
            self.set_current_pos(x0-1, y0)
            return True
        except IndexError:
            print("\nYou rest on the wall, choose a different direction\n")
            return False

    def move_down(self):
        """
        Mode down method
        """
        x0, y0 = self.__current_pos
        try:
            _ = self.rooms[x0+1][y0]
            self.set_current_pos(x0+1, y0)
            return True
        except IndexError:
            print("\nYou rest on the wall, choose a different direction\n")
            return False

    def move_right(self):
        """
        Move right method
        """
        x0, y0 = self.__current_pos
        try:
            _ = self.rooms[x0][y0+1]
            self.set_current_pos(x0, y0+1)
            return True
        except IndexError:
            print("\nYou rest on the wall, choose a different direction\n")
            return False
    
    def get_current_room_information(self):
        """
        Get current room method
        """
        return self.rooms[self.__current_pos[0]][self.__current_pos[1]]

    def move_left(self):
        """
        Move left method
        """
        x0, y0 = self.__current_pos
        try:
            if y0-1 < 0:
                raise IndexError
            _ = self.rooms[x0][y0-1]
            self.set_current_pos(x0, y0-1)
            return True
        except IndexError:
            print("\nYou rest on the wall, choose a different direction\n")
            return False

    def show_map(self):
        """
        Show map method
        """
        x0, y0 = self.__current_pos
        for i in range(self.size):
            line = ''
            for j in range(self.size):
                if i == x0 and j == y0:
                    line += '@'
                else:
                    line += '-'
            print(line)
