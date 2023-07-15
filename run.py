from termcolor import colored, cprint
import time
inventory_dict = {}
delay = 1
logo = (colored('THE ESCAPE FROM THE WIZARDS LAIR', 'yellow', attrs=['bold']))
user_command = ''

class Location:
    def __init__(self, description, short_description, new_description, description1, description2, directions):
        self.description = description
        self.short_description = short_description
        self.new_description = new_description
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.usables = {}
        self.visited = False
        self.name = None
        self.interactible = {}
        self.directions = directions
        self.description1 = description1
        self.description2 = description2

teleportation_chamber = Location('''
A vaulted room illuminted by strange glowing symbols
 in the stonewalls\n.
In the center of the room is a pentagram painted on
 the floor surrounded by lit white candles.\n
In a black shelf you see a glass vial with a label of a skull.
In a corner stands a red round table.\n
A gold KEY is on the table.''', '''You are in the 
teleportation-chamber.''', '', 'description1', 'description2', 'directions')
teleportation_chamber.name = 'Teleportation Chamber'
teleportation_chamber.short_description = 'You are in the teleportation-chamber.'
teleportation_chamber.new_description = '''
a vaulted room illuminted by strange glowing symbols
 in the stonewalls\n.
In the center of the room is a pentagram painted
 on the floor surrounded by lit white candles.\n
In a corner stands a red round table.'''
teleportation_chamber.description1 = ''
teleportation_chamber.description2 = ''
teleportation_chamber.directions = 'You can go: North, East, South, West'

teleportation_chamber.usables = {  
}

library = Location('''five shelves are filled with jars, bottles and strange,
instruments and burning candels.\n''', 'a dimly lit potions chamber.', 'This is the new description.', 'description1', 'description2', 'directions')
library.directions = 'You can go: West'
library.new_description = '''five shelves are filled with jars, bottles and strange,
instruments and burning candels.\n
On a black table stands lonely.'''
library.description1 = '''
A instained parchment with the words "Fetchspell" lies on the table.\n'''
library.description2 = '''A parchment with the words "icespell" lies on the table.'''

library.interactible = {
  "icespell": "A spell with that turns things very cold.",
  "fetchspell": "Get things far away from you." 
}

control_room = Location('''this bright control-room is allmost entirely filled
 with computerscreens, buttons and levers. 
 In the center is a large controlpanel.\n
 On a coathanger you see a blue and yellow cloak.''', ' a room filled with computers and machines.', 'This is the new description.', 'description1', 'description2', 'directions')
control_room.directions = 'You can go: East'
control_room.description1 = ''
control_room.description2 = ''
control_room.interactible = {
  "cloak": "A cloak of invisibility!",
}

hallway = Location('''this hallway continues ends in total darkness.''', ' a dark hallway.', 'This is the new description.', 'description1', 'description2', 'directions')
hallway.directions = 'You can go: East'
hallway.description1 = ''
hallway.description2 = ''
wizards_room = Location('''the old wizard is snoozing in a arge armchair in front of a large fireplace.
 In his lap you see a key.''', ' the wizards home. Quite cozy.', '''the old wizard is snoozing in a arge armchair 
in front of a large fireplace. Cozy.''', 'description1', 'description2', 'directions')
wizards_room.directions = 'You can go: North'
wizards_room.description1 = ''
wizards_room.description2 = ''
teleportation_chamber.new_description = '''the old wizard is snoozing in a arge armchair 
in front of a large fireplace. Cozy.'''

dragon_keep = Location(''' large cavern. High above you can see an opening
 beaming with daylight. A large red dragon is lying in the center of the cavern.
  It is held down with a massive locked chain.
  It looks at you with sad eyes and speaks.\n
  Please help me! If you unlock my chains you can leave this place in my back as I fly away!
  ''', ' a large sad, red dragon.', 'This is the new description.', 'description1', 'description2', 'directions')

dragon_keep.description1 = ''
dragon_keep.description2 = ''
dragon_keep.directions = 'You can go: East'
pool = Location(''' a wooden platform, a black icy cold pool stretches across the long chamber and 
ends in an identical wooden platform on the other side.
There is no way to cross it.''', 'a large black pool, icy cold.', 'This is the new description.', 'description1', 'description2', 'directions')
pool.description1 = 'A cat purrs.'
pool.description2 = ''
pool.directions = 'You can go: South'

teleportation_chamber.south = wizards_room
teleportation_chamber.north = pool
teleportation_chamber.west = control_room
teleportation_chamber.east = library

wizards_room.north = teleportation_chamber
#pool.west = dragon_keep
pool.south = teleportation_chamber

dragon_keep.east = pool

control_room.east = teleportation_chamber

library.west = teleportation_chamber

current_location = teleportation_chamber

def help():
    print('##################################################################')
    print('#  The game is played with these commands:                       #')
    print('#                                                                #')
    print('#  help : Brings up this list.                                   #')
    print('#                                                                #')
    print('#  inventory : Shows your current items                          #')
    print('#                                                                #')
    print('#  look : Shows your surroundings.                               #')
    print('#                                                                #')
    print('#  examine + item: A description of an item or thing.            #')
    print('#                                                                #')
    print('#  hold + item : Description of an item in your inventory.       #')
    print('#                                                                #')
    print('#  use + item : Use item in the inventory, or in a location.     #')
    print('#                                                                #')
    print('#  take + item : Take something and add to the inventory.        #')
    print('#                                                                #')
    print('#  Some words are specific to special locations, and will        #')
    print('#  not work anywhere else.                                       #')
    print('##################################################################')

def intro():
    print(colored('''
Everything is black.\n
As your head clears you are greeted by an old wizard in red robes. 
You realize you stand in a pentagram. You have been teleported here!\n
"Greetings. I am in need of a new assistent. My old one is ... no longer
 available."\n
"Get yourself settled and do not even think of escaping.
There is no way out of here."\n
He walks away and leaves you in a state of shock and enger. \n
No way you are staying here! Time to find a way out.
    ''', 'cyan'))
    input('press ENTER to continue.\n')
    print('You are in the ' + current_location.name + '. You see ' + current_location.description + current_location.description1 + current_location.description2)
    print('\n')
    current_location.visited = True
    print(colored('Available Directions : ' , 'yellow') + current_location.directions)

def dragon_isfree():
    print('Congratilations!\n')
    print('You climb into the dragons scaly back and hold on tight.\n')
    print('With a roar the dragon spreads its wings and leaps up into the air.\n')
    print('With three flaps of its mighty wings, you emerge into the cold air high above the prison.')
    print('Game Over')
    exit()

def examine():

    if user_command.startswith('xa'):
        #if item that user types exist in the list items, it is removed and added to the users inverntorylist.
        #The description of the location is changed to reflect that the object is no longer there.
        for item in current_location.interactible.keys():
            if user_command.endswith(item):
                value= current_location.interactible.get(item)
                print(value)
                print('In the location: ')
                break
        else:
            print('You can not examine that.\n')

def gameloop():
    current_location = teleportation_chamber
    user_command = ''
    inventory_isempty = True
    ice_taken = False
    fetch_taken = False
    pool_isfrozen = False

    while user_command != 'quit':
       
        print('')
        x = input(colored('What do you do now? > ', 'green'))
        user_command = x.lower()
        loc = current_location
        print('\n')
        #makes sure every input is lowercase to avoid errors.

        # The if statement checks if the user can go in all directions. If not
        # then a message is printed and the gameloop starts over.
        if user_command == 'north':
            try:
                if user_command is not None:
                    if current_location.directions is not None:
                        current_location = current_location.north
                        if current_location.visited == False: 
                            print('You see ' + current_location.description + current_location.description1 + current_location.description2 + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                            current_location.visited = True
                        else:
                            print(current_location.directions)
                            print('You see ' + current_location.short_description + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                
            except AttributeError:
                print(colored('Wrong direction. Choose again.', 'red'))
                current_location = loc
                pass

        elif user_command == 'south':
            try:
                if user_command is not None:
                    if current_location.directions is not None:
                        current_location = current_location.south
                        if current_location.visited == False: 
                            print('You see ' + current_location.description + current_location.description1 + current_location.description2 + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                            current_location.visited = True
                        else:
                            print(current_location.directions)
                            print('You see ' + current_location.short_description + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                
            except AttributeError:
                print(colored('Wrong direction. Choose again.', 'red'))
                current_location = loc
                pass

        elif user_command == 'east':
            try:
                if user_command is not None:
                    if current_location.directions is not None:
                        current_location = current_location.east
                        if current_location.visited == False:
                            print('You see ' + current_location.description + current_location.description1 + current_location.description2 + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                            current_location.visited = True
                        else:
                            print(current_location.directions)
                            print('You see ' + current_location.short_description + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                
            except AttributeError:
                print(colored('Wrong direction. Choose again.', 'red'))
                current_location = loc
                pass

        elif user_command == 'west':
            try:
                if user_command is not None:
                    if current_location.directions is not None:
                        current_location = current_location.west
                        if current_location.visited == False:
                            print('You see ' + current_location.description + current_location.description1 + current_location.description2 + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                            current_location.visited = True
                        else:
                            print(current_location.directions)
                            print('You see ' + current_location.short_description + '\n')
                            print(colored('Available Directions : ' , 'yellow') + current_location.directions)
                
            except AttributeError:
                print(colored('Wrong direction. Choose again.', 'red'))
                current_location = loc
                pass

        elif user_command.startswith('use') and current_location == dragon_keep:
            for item in inventory_dict.keys():
                if item == 'key':
                    if user_command.endswith('key'):
                        print('You use the key to unlock the chains around the dragons neck.')
                        dragon_isfree()
                        break
            else:
                print('That did not work.')

        elif user_command.startswith('use') and current_location == pool:
            if pool_isfrozen == False:
                for item in inventory_dict.keys():
                    if user_command.endswith('icespell'):
                        print('You use the ice spell to freeze the water solid!')
                        current_location.west = dragon_keep
                        current_location.directions = 'You can go: South, West'
                        current_location.description ='''
a wooden platform, shiny frozen pool stretches across the long chamber and 
ends in an identical wooden platform on the other side.\n
The air is very cold.'''
                        pool_isfrozen = True
                        break
                else:
                    print('That did not work.')
            else:
                print('The pool is allready frozen.')
        elif user_command.startswith('use') and current_location == wizards_room:
            for item in inventory_dict.keys():
                if user_command.endswith('fetchspell'):
                    print('You use the fetchspell to get the key!')
                    print('Thanks you your clever use of the spell, the wizard snoozes on.')
                    inventory_isempty = False
                    inventory_dict["key"] = "A golden key skaped like a dragon."
                    current_location.description = current_location.new_description
                    break
            
                else:
                    print('Hmm. Maby use something else.')
        
        elif user_command.startswith('take') and current_location == wizards_room:
            print('You can not risk it. He will wake up.')
        
        elif user_command.startswith('take'):
            inventory_isempty = False
            for item in current_location.interactible.keys():
                if user_command.endswith('icespell') and ice_taken == False:
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description2= ''
                        ice_taken = True
                        break

                elif user_command.endswith('fetchspell') and fetch_taken == False:
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description1 = ''
                        fetch_taken = True
                        break
#if item that user types exist in the list items, it is removed and added to the users inverntorylist.
            #The description of the location is changed to reflect that the object is no longer there.
                elif user_command.endswith(item):
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description = current_location.new_description
                        break
                    
            else:
                print('You can not take that.\n')
        
        elif user_command.startswith('examine') and current_location == wizards_room:
            if user_command.endswith('key'):
                print('It is a small gold key in the shape of a dragon.')
            elif user_command.endswith('wizard'):
                print('The Wizard looks very old. The long hair and beard is white.')
                print('He is dressed in a red robe decorated with magic runes.')
                print("Strange. He doesn't look dangerous, but he is.")
            else:
                for item in current_location.interactible.keys():
                    if user_command.endswith(item):
                        value= current_location.interactible.get(item)
                        print(value)
                        print('Is in the location.')
                        break
                else:
                    print('You can not examine that.\n')

        elif user_command.startswith('examine') and current_location == wizards_room:
            if user_command.endswith('wizard'):
                print('The Wizard looks very old. The long hair and beard is white.')
                print('He is dressed in a red robe decorated with magic runes.')
                print("Strange. He doesn't look dangerous, but he is.")

        elif user_command.startswith('examine'):
            for item in current_location.interactible.keys():
                if user_command.endswith(item):
                    value= current_location.interactible.get(item)
                    print(value)
                    print('Is in the location.')
                    break
            else:
                print('You can not examine that.\n')

        elif user_command.startswith('hold'):
            for item in inventory_dict.keys():
                if user_command.endswith(item):
                    value= inventory_dict.get(item)
                    print(value)
                    print('Is in your inventory.')
                    break
            else:
                 print('Not in your inventory')
                 
        elif user_command.startswith('inventory'):
            if inventory_isempty == False:
                for x, y in inventory_dict.items():
                    print('You have: ' + x, 'Descpription: ' + y)
            else:
                print('Inventry is empty')

        elif user_command.startswith('look'):
            
            try:
                if user_command is not None:
                    if current_location.directions is not None:
                        
                        print('You see' + current_location.description + ' ' + current_location.description1 + ' ' + current_location.description2)
                        print('\n')
                        print(colored('Available Directions : ' , 'yellow') + current_location.directions + '\n')  
                
            except AttributeError:
                print(colored('Wrong direction. Choose again.', 'red'))
                pass
            
        elif user_command == 'help':
            help()

        elif user_command == 'quit':
            print('Good Bye')
            current_location = ''
            #sets to avoid getting the AttributeError = 'NoneType'
        else:
            print('That did not seem to work. Type something else.')
    print('QUITTING GAME')

print('Welcome to the text-adventure ' + logo)
print('')
user_name = input('What is your name, adventurer? > ')
print('') 
print('Good to meet you ' + (colored(user_name, 'green')) 
+ ', now let us begin.\n')
intro()
gameloop()