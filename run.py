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
''', '''You are in the 
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
instruments and burning candels.'''
library.description1 = '''
You see a inkstained parchment with the words "Fetchspell" sticking out of a book.\n'''
library.description2 = ''
library.interactible = {
    "fetchspell": "A spell to get things far away." 
}

library_gate = Location(''' a large black iron gate blocks the entrance to the library.\n
You can tell by the large sign above the gate that says:\n
"LIBRARY". But why is it closed?\n
There is no keyhole, so it must be opened somewhere else.\n''', 'a dimly lit potions chamber.', 'This is the new description.', 'description1', 'description2', 'directions')
library_gate.directions = 'You can go: West'
library_gate.new_description = ' a large iron gate. It is open.'
library_gate.description1 = ''
library_gate.description2 = ''

garden = Location(''' a lush garden spreads out like a jungle. Trees, bushes and 
greenhouses frow everything from bananas to potatoes.
Racks and barrels are filled with gardeningtools.
On a sturdy wooden table are hundreds of seeds and a bowl full of beans.\n''', 'a lush garden.', 'This is the new description.', 'description1', 'description2', 'directions')
garden.directions = 'You can go: South'
garden.new_description = ''
garden.description1 = '''
A glass bottle labelled "Plantfood" stands on the table..\n'''
garden.description2 = ''

garden.interactible = {
  "plantfood": "A bottle of super plantfood.",
  "bean": "A green magic bean!" 
}

potions = Location('''five shelves are filled with jars, bottles and strange,
instruments and burning candels.\n''', 'a dimly lit potions chamber.', 'This is the new description.', 'description1', 'description2', 'directions')
potions.directions = 'You can go: West'
potions.new_description = '''five shelves are filled with jars, bottles and strange,
instruments and burning candels.\n
On a black table stands lonely.'''
potions.description1 = ''
potions.description2 = '''A parchment with the words "icespell" lies on the table.'''

potions.interactible = {
  "icespell": "A spell with that turns things very cold.",
}

control_room = Location('''this dark control-room pulsates with neon-lights of red, green and blue.
It is allmost entirely filled with screens, buttons and levers. 
In the center is a large controlpanel.\n
Under a copper-plaque that reads "Library" you see three buttons.
A square-button, a circle-button and a triangle-button.''', ' a control-room filled with machines and neon light.', 'This is the new description.', 'description1', 'description2', 'directions')
control_room.directions = 'You can go: East'
control_room.description1 = ''
control_room.description2 = ''
control_room.usables = {
"square": "A button shaped like a SQUARE.",
"circle": "A button shaped like a CIRCLE.",
"triangle": "A button shaped like a TRIANGLE."
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

hallway1 = Location('''a hallway with a flor of blue marble. A glowing yellow orb hovers in the ceiling.''', ' a hallway with a blue marble floor.', 'This is the new description.', 'description1', 'description2', 'directions')
hallway1.directions = 'You can go: East, West, South'
hallway1.description1 = ''
hallway1.description2 = ''

hallway2 = Location('''a hallway entirely painted red. four wallmounted torches illuminates the room.
A cool breeze from the north makes the torches flames dance.''', ' a hallway painted red. Torches flicker in a breeze', 'This is the new description.', 'description1', 'description2', 'directions')
hallway2.directions = 'You can go: East, West, South, North'
hallway2.description1 = ''
hallway2.description2 = ''

hallway3 = Location('''a black and white hallway with checkered floor is illusmitaed by four white glowing 
orbs, slowly pulsating. You stop and wonder if there are small pixies in there.''', ' a hallway with checkered floor lit by four white orbs.', 'This is the new description.', 'description1', 'description2', 'directions')
hallway3.directions = 'You can go: East'
hallway3.description1 = ''
hallway3.description2 = ''

guard_room = Location('''a room filled with beds, chests, weapond and armor on racks, 
and a general mess of clothes and items over the floor and chairs.\n
Three ugly trolls look up as you enter.\n
They do not look friendly, or like they are having a good day.
''', ' a messy guardroom with three angry trolls in it.', 'This is the new description.', 'description1', 'description2', 'directions')
guard_room.directions = 'You can go: West'
guard_room.description1 = ''
guard_room.description2 = ''

observatory= Location('''a round room with a domed ceiling.\n
On the soft blue carpet stands a comfortable-looking armchair. A large chrystal chandelier
 is hanging from the ceiling.
Directly below the chandelier is a yellow flowerpot.
The main focus of the room however is the large gold telescope pointing up at the dome.''', ' a round room with a telescope in the center. An observatory.', 'This is the new description.', 'description1', 'description2', 'directions')
observatory.directions = 'You can go: North'
observatory.description1 = 'Something is hanging up in the chandelier. A cloak!'
observatory.description2 = ''

observatory.usables = {
"cloak": "A cloak decorated with silver closed eyes.",
"telescope" : "A beautiful large telescope."
}

teleportation_chamber.south = wizards_room
teleportation_chamber.north = hallway2
teleportation_chamber.west = hallway3
teleportation_chamber.east = hallway1

potions.west = hallway1

hallway1.west = teleportation_chamber
hallway1.east = potions
hallway1.south = observatory

hallway2.north = pool
hallway2.south = teleportation_chamber
hallway2.west = control_room
hallway2.east = guard_room

hallway3.east = teleportation_chamber

observatory.north = hallway1

guard_room.west = hallway2

wizards_room.north = teleportation_chamber

#pool.north = garden
#pool.east = library_gate
#pool.west = dragon_keep
pool.south = hallway2

dragon_keep.east = pool

control_room.east = hallway2

#library_gate.east = library
library_gatewest = pool

library.west = pool
library_gate.west = pool

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
    square_ispressed = False
    triangle_ispressed = False
    circle_ispressed = False
    library_isopen = False
    invisible = False
    bean_isplanted = False
    plantfood_isused = False

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
                        current_location.east = library_gate
                        current_location.north = garden
                        current_location.directions = 'You can go: South, West, North, East'
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
            if user_command.endswith('key'):
                print('You can not risk it. He will wake up.')
            elif user_command.endswith('wizard'):
                print('He is way to heavy. And why would you want him?')
            else:
                print('You can not take that.')

#use item from usable that can not be taken

        elif user_command.startswith('use') and current_location == control_room:
            
            if invisible == True:
                if user_command.endswith('square'):    
                    for item in current_location.usables.keys():
                        if item == 'square':
                            #if user_command.endswith('square'):
                            # item = 'square'
                            value= current_location.usables.get(item)
                            square_ispressed = True
                            #if square_ispressed == False:
                            print('You press the ' + value + 'key' + '\n')
                            x = input(colored('The square turns green. Next button please. > ', 'green'))
                            user_command = x.lower()
                            #input('Enter next symbol.')
                            #current_location.description2= ''
                            
                            if user_command.startswith('use') and current_location == control_room:
                                #if invisible == True:
                                if user_command.endswith('triangle'):    
                                    for item in current_location.usables.keys():
                                        if item == 'triangle':
                                            #if user_command.endswith('square'):
                                            # item = 'square'
                                            value= current_location.usables.get(item)
                                            triangle_ispressed = True
                                            #if square_ispressed == False:
                                            print('You press the ' + value + 'key' + '\n')
                                            x = input(colored('The triangle turns green. Next button please. > ', 'green'))
                                            user_command = x.lower()
                                            #input('Enter next symbol.')
                                            #current_location.description2= ''
                            
                                            if user_command.startswith('use') and current_location == control_room:
                                                #if invisible == True:
                                                if user_command.endswith('circle'):    
                                                    for item in current_location.usables.keys():
                                                        if item == 'circle':
                                                            #if user_command.endswith('square'):
                                                            # item = 'square'
                                                            value= current_location.usables.get(item)
                                                            circle_ispressed = True
                                                            #if square_ispressed == False:
                                                            print('You press the ' + value + 'key' + '\n')
                                                            print('The square, triangle and circle flash green.')
                                                            print('A symbol of a gate appears just above the buttons. What did you just do?')
                                                            #current_location.description2= ''
                                                else:
                                                    print('The buttons go red. That was not the right sequence.')
                                                    circle_ispressed = False
                                                    square_ispressed = False
                                                    triangle_ispressed = False
                                                    break
                    
                                else:
                                    print('The buttons go red. That was not the right sequence.')
                                    circle_ispressed = False
                                    square_ispressed = False
                                    triangle_ispressed = False
                                    break

                elif user_command.endswith('triangle'):
                    print('The buttons go red. That was not the right sequence.') 
                elif user_command.endswith('circle'):
                    print('The buttons go red. That was not the right sequence.') 
                else:
                    print('Try something else.')
            elif user_command.endswith('cloak'):
                for item in inventory_dict.keys():
                    if user_command.endswith('cloak'):
                        print('You wear the cloak and become invisible!')
                        invisible = True
                        break
                else:
                    print('That did not work.')

            
            elif user_command.endswith('square'):    
                print('The troll sees you and pushes you back.')
                print('GET AWAY FROM THEM CONTROLS, YA WIMP.')
                print('As long as he can see you, you can not get close.')
            elif user_command.endswith('triangle'):    
                print('The troll sees you and pushes you back.')
                print('GET AWAY FROM THEM CONTROLS, YA WIMP.')
                print('As long as he can see you, you can not get close.')
            elif user_command.endswith('circle'):    
                    print('The troll sees you and pushes you back.')
                    print('GET AWAY FROM THEM CONTROLS, YA WIMP.')
                    print('As long as he can see you, you can not get close.')

            else:
                ('That does not seem to work.')


        
        elif user_command.startswith('take'):
            inventory_isempty = False
            for item in current_location.interactible.keys():
                if user_command.endswith('icespell') and current_location == potions:
                        item = 'icespell'
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description2= ''
                        
                        break

                elif user_command.endswith('fetchspell') and current_location == library:
                        item = 'fetchspell'
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description1 = ''
                        
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

        elif user_command.startswith('examine') and current_location == pool:
            if user_command.endswith('platform'):
                print('Just wooden boards nailed together.')
                print('Nothing special about it.')
            elif user_command.endswith('water') and pool_isfrozen == False:
                print('The water is icy cold and black.')
                print('You will die in seconds if you jump in.')
            elif user_command.endswith('water') and pool_isfrozen == True:
                print('The water completely frozen solid now')
                print('That spell really works.')    
            else:
                for item in current_location.interactible.keys():
                    if user_command.endswith(item):
                        value= current_location.interactible.get(item)
                        print(value)
                        print('Is in the location.')
                        break
                else:
                    print('You can not examine that.\n')
            

        elif user_command.startswith('examine'):
            for item in current_location.interactible.keys():
                if user_command.endswith(item):
                    value= current_location.interactible.get(item)
                    print(value)
                    print('Is in the location.')
                    break

            for item in current_location.usables.keys():
                if user_command.endswith(item):
                    value= current_location.usables.get(item)
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