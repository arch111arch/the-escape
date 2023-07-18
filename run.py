from termcolor import colored, cprint
import time
inventory_dict = {}
delay = 1
logo = (colored('THE ESCAPE FROM THE WIZARDS LAIR', 'yellow', attrs=['bold']))
user_command = ''


class Location:
    def __init__(self, description, short_description,
    new_description, description1, description2, directions):
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
        self.inter = False
        self.usab = False


teleportation_chamber = Location(''' a vaulted room illuminated by strange glowing symbols cut in the stonewalls.\n
In the center of the room is a pentagram painted on the floor,\n
surrounded by lit white candles.\n
Strange artefacts and gadgets and magical instruments fill shelves that\n
reach the ceiling.
''', ' the teleportation-chamber.', '', '', '', '')
teleportation_chamber.name = 'Teleportation Chamber'
teleportation_chamber.short_description = 'You are in the teleportation-chamber.'
teleportation_chamber.new_description = ''
teleportation_chamber.description1 = ''
teleportation_chamber.description2 = ''
teleportation_chamber.directions = 'You can go: North, East, South, West'
teleportation_chamber.usables = {}

library = Location(''' a rectangular room entirely furnished with boookshelves.\n
These books are above your level and most languages you do not even\n
recognise. This was locked for a reason though, so you search\n
for something you can use.
''', 'a impressive magic-library', '', '', '', '')
library.directions = 'You can go: West'
library.new_description = ''
library.description1 = '''
You see a inkstained parchment with the words "Fetchspell" sticking out of a book.\n'''
library.description2 = ''
library.interactible = {"fetchspell": "A spell to get things far away."}
library.inter = True

library_gate = Location(''' a large black iron gate blocks the entrance to the library.\n
 You can tell by the large sign above the gate that says: "LIBRARY".\n
 But why is it closed?\n
 There is no keyhole,it be opened somewhere else.\n''', 'a gate to the Library.', '', '', '', '')
library_gate.directions = 'You can go: West'
library_gate.new_description = ' a large iron gate. It is open.'
library_gate.description1 = ''
library_gate.description2 = ''

garden = Location(''' a lush garden spreads out like a jungle.\n
 You see trees, bushes and greenhouses frow everything from bananas to potatoes.\n
 Racks and barrels are filled with gardeningtool that does not interest you.\n
On a worn sturdy wooden table,\n
are hundreds of seeds and bags of soil.\n''', 'a lush garden.', '', '', '', '')
garden.directions = 'You can go: South'
garden.new_description = ''
garden.description1 = 'A glass bottle labelled "plantfood" stands on the table.'
garden.description2 = 'An jar of beans is one the table.'

garden.interactible = {
  "plantfood": "A bottle of super plantfood.",
  "beans": "A jar of green magic beans!",
}
garden.inter = True

potions = Location(''' five shelves are filled with jars, bottles and strange, instruments\n
and burning candles.\n
A black table is to your left.
''', 'a dimly lit potions chamber.', '', '', '', '')
potions.directions = 'You can go: West'
potions.new_description = '''
 five shelves are filled with jars, bottles and strange, instruments\n
and burning candles.\n
A black table is to your left.
'''
potions.description1 = ''
potions.description2 = '''A parchment with the words "icespell" lies on the table.'''

potions.interactible = {
  "icespell": "A spell with that turns things very cold.",
}
potions.inter = True

control_room = Location(''' a dark control-room pulsates with neon-lights of red, green and blue.\n
It is allmost entirely filled with screens, buttons and levers.\n
In the center is a large controlpanel with a copper sign that reads:\n
"Library". Under it you see three buttons that shine red.\n
One is a square, one is a circle and one is a triangle.\n
You have seen one like this before, you need to enter a code.
\n
A big bored troll in a black uniform sits typing on a keyboard.\n
He did not notice you.
''', ' a control-room filled with machines and neon lights.', '', '', '', '')
control_room.directions = 'You can go: East'
control_room.description1 = ''
control_room.description2 = ''
control_room.usables = {
"square": "A button shaped like a SQUARE.",
"circle": "A button shaped like a CIRCLE.",
"triangle": "A button shaped like a TRIANGLE."
}
control_room.usab = True

wizards_room = Location(''' the old wizard is snoozing in a arge armchair in front of a large fireplace.\n
 In his lap you see a key.\n
 The room is cozy with a big bed, plenty of shelves with books and trinkets, drawers,\n
 A table and a chair and the large red chair he is sitting in.
 ''', ' the wizards home. Quite cozy.', '''the old wizard is snoozing in a arge armchair
in front of a large fireplace. Cozy.''', '', '', '')
wizards_room.directions = 'You can go: North'
wizards_room.description1 = ''
wizards_room.description2 = ''
teleportation_chamber.new_description = ''' the old wizard is snoozing in a arge armchair in front of a large fireplace.\n
 The room is cozy with a big bed, plenty of shelves with books and trinkets, drawers,\n
 A table and a chair and the large red chair he is sitting in.
 '''

dragon_keep = Location(''' a large rocky smoky cave. High above you can see an opening\n
beaming with daylight.\n
A large red dragon is lying in the center of the cave.
It is held down with a massive chain, connected to a big lock.\n
The dragon looks at you with sad eyes and speaks.\n
"Please help me! The wizard imprisoned me here for years now.\n
I want to fly home to my mountain and live in peace.\n
If you unlock my chains you can leave this place in my back as I fly away!\n
Find a key that looks like a dragon and return here."
  ''', ' a large sad, red dragon in a smoky cave.', '', '', '', '')

dragon_keep.description1 = ''
dragon_keep.description2 = ''
dragon_keep.directions = 'You can go: East'

pool = Location(''' a wooden platform, a black icy cold pool stretches across the long chamber\n
and ends in an identical wooden platform on the other side.\n
There is no way to cross the pool.\n
You see a caveopening to the west. To the east you see a doorway.\n
You just can not get to them.
''', 'a large black pool, icy cold.', '', '', '', '')
pool.description1 = ''
pool.description2 = ''
pool.directions = 'You can go: South'

hallway1 = Location(''' a hallway with a flor of blue marble.\n
A glowing yellow orb hovers in the ceiling.''', ' a hallway with a blue marble floor.', '', '', '', '')
hallway1.directions = 'You can go: East, West, South'
hallway1.description1 = ''
hallway1.description2 = ''

hallway2 = Location(''' a hallway entirely painted red. four wallmounted torches illuminates the room.\n
A cool breeze from the north makes the torches flames dance.
A doorway leads to the west. A doorway leeds to the east.\n
A dark large opening continues to the north.\n
''', ' a hallway painted red. Torches flicker in a breeze', '', '', '', '')
hallway2.directions = 'You can go: East, West, South, North'
hallway2.description1 = ''
hallway2.description2 = ''

hallway3 = Location(''' a black and white hallway with checkered floor.\n
Is illusmitaed by four white glowing orbs, slowly pulsating.\n
You stop and wonder if there are small pixies in there.\n
You can see the servants-quarters, bathrooms, kitchens and storerooms ahead.\n
But you can not find any reason for you to go in there.\n
No way you are going to be a servant like this!\n
''', ' a hallway with checkered floor lit by four white orbs.', '', '', '', '')
hallway3.directions = 'You can go: East'
hallway3.description1 = 'A small handwritten note is on the floor.'
hallway3.description2 = ''
hallway3.interactible = {
  "note": "Remember: Square, triangle, circle.",
}
hallway3.inter = True

guard_room = Location(''' a room filled with beds, chests, weapond and armor on racks, and a general mess\n
of clothes and items over the floor and chairs.\n
Three ugly trolls look up as you enter.\n
They do not look friendly, or like they are having a good day.\n
There is nothing for you to do in here.\n
Better hurry and find a way to escape before they come after you.
''', ' a messy guardroom with three angry trolls in it.', '', '', '', '')
guard_room.directions = 'You can go: West'
guard_room.description1 = ''
guard_room.description2 = ''

guard_room.usables = {"trolls": "Ugly, mean-looking and very dirty.",}
guard_room.usab = True

observatory = Location(''' a round room with a domed ceiling.\n
On the soft blue carpet stands a comfortable-looking armchair.\n
A large chrystal chandelier is hanging from the ceiling.\n
The main focus of the room however is the large gold telescope.\n
It is pointing up at the dome.''', ' a round room with a telescope in the center.', '', '', '', '')
observatory.directions = 'You can go: North'
observatory.description1 = '''\nSomething is hanging up in the chandelier. A cloak!\n
Is that ... an invisibility cloak? They are super rare.'''
observatory.description2 = 'Directly below the chandelier is a yellow flowerpot.'

observatory.usables = {
"cloak": "A cloak decorated with silver closed eyes.",
"telescope" : "A beautiful large telescope.",
"flowerpot" : "A large yellow flowerpot. Nothing is growing in it."
}
observatory.usab = True

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

library.west = pool
library_gate.west = pool
#library_gate.east = library

garden.south = pool

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
Where are you? You were just running errands for your teacher in the\n
school for magic where you are a student.\n
As your head clears you are greeted by an old wizard in red robes.\n
Immediately you recignise that face. This is the wanted wizard\n
Araval the Red. What is going in here?\n
\n
You realize you stand in a pentagram. You have been teleported here!\n
"Greetings. I am in need of a new assistent." he tells you.\n
"My old one is ... no longer available. Nasty business.
I would advice you not to make the trolls angry.
I would like to keep you around longer than the last one."\n
"Get yourself settled and do not even think of escaping.\n
There is no way out of here."\n
He walks away to the south and leaves you in a state of shock and anger. \n
\n
No way you are staying here!\n
Time to find a way out of here!
    ''', 'cyan'))
    input('press ENTER to continue.\n')
    print('You are in the ' + current_location.name + '.\n')
    print('You see ' + teleportation_chamber.description)
    current_location.visited = True
    print(colored('Available Directions : ' , 'yellow') + current_location.directions)

def dragon_isfree():
    print('CONGRATULATIONS!\n')
    print('You used your wits to find all the peices nedded to escape.')
    print('You climb onto the dragons scaly back and hold on tight.\n')
    print("Let's get out of here!"+ ' the dragon says, smiling.' )
    print('With a roar the dragon spreads its wings and leaps up into the air.\n')
    print('With three flaps of its mighty wings, you emerge into the cold air high above the prison.')
    print('You have escaped and completed the game!')
    print('')
    print('Game Over')
    exit()

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
    climbed_beanstalk = False

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
                        current_location.description1 = 'You can now enter the cave to the West,\n'+' or walk across the ice to a doorway in the North,\n'+ ' or enter a doorway to the East.'
                        current_location.short_description = 'a solidly frozen pool. Hey, you can skate here.'
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

        elif user_command.startswith('use') and current_location == observatory:
            if user_command.endswith('telescope'):
                print('Amazing! You see stars and planets in the dark space.')
                print('A unicorn is running on a pink spacecloud.')
                print('Wait what?')
                print('As you step away from the telescope, you shake your head.')

            elif bean_isplanted == False:
                for item in inventory_dict.keys():
                    if user_command.endswith('beans'):
                        print('You plant a handfull of beans in the flowerpot.')
                        print('Now you just needs somehting to make it grow.')
                        current_location.usables.update({"flowerpot": 'You have planted magic beans in here.'})
                        bean_isplanted = True
                        current_location.description2 = 'Directly below the chandelier is a yellow flowerpot.'+'\nThere are beans planted in there.'
                        break
                else:
                    print('Hmm. Maby plant something?.')
            
            elif user_command.endswith('beans') and bean_isplanted == True:
                print('You have allready planted beans here.')
            
            elif plantfood_isused == False:
                if bean_isplanted == True:
                    for item in inventory_dict.keys():
                        if user_command.endswith('plantfood'):
                            print('You pour the super plantfood into the pot.')
                            print('Somethings happening. Leaves start to grow very fast.')
                            print('A massive beanstalk shootes up into the ceiling, right past the chandelier.')
                            current_location.usables.update({"flowerpot": 'What a magnificent beanstalk!'})
                            plantfood_isused = True
                            current_location.description2 = 'Directly below the chandelier is a yellow flowerpot.'+'\nA massive beanstalk reackes all the way to the ceiling.'
                            break
                else:
                    print('You need to plant something first before you can use plantfood.')
             
            elif user_command.endswith('plantfood') and plantfood_isused == True:
                print('The beanstalk is as big as it is going to get.')

            elif climbed_beanstalk == False:
                if plantfood_isused == True:
                    if user_command.endswith('beanstalk'):
                        print('You climb up the beanstalk all the way to the top.')
                        print('While you are up there, you grab the cloak from the chandelier.')
                        print('You climb down again, putting the cloak into your inventory.')
                        inventory_dict["cloak"] = "A cloak decorated with closed silver eyes."
                        current_location.usables.pop("cloak")
                        climbed_beanstalk = True
                        current_location.description1 = 'Vines are covering the entire chandelier now.'

            else:
                print('That was not right.')

        elif user_command == 'use beanstalk' and current_location == observatory:
            if climbed_beanstalk == True:
                print('No way you are climbing that thing again.')

        elif user_command.startswith('use') and current_location == observatory:
            if plantfood_isused == True:
                if user_command.endswith('beanstalk'):
                    print('You climb up the beanstalk all the way to the top.')
                    print('While you are up there, you grab the cloak from the chandelier.')
                    print('You climb down again, putting the cloak into your inventory.')
                    inventory_dict["cloak"] = "A cloak decorated with closed silver eyes."
                    current_location.usables.pop("cloak")
                    current_location.description1 = 'Vines are covering the entire chandelier now.'
                    climbed_beanstalk = True
                    break
            
            elif user_command.endswith('beans') and plantfood_isused == True:
                print('Maby you can use something else than beans?')
            else:
                print('That did not work.')
        
        elif user_command.startswith('take') and current_location == wizards_room:
            if user_command.endswith('key'):
                print('You can not risk it. He will wake up.')
            elif user_command.endswith('wizard'):
                print('He is way to heavy. And why would you want him?')
            else:
                print('You can not take that.')

#use item from usable that can not be taken

        elif user_command.startswith('use') and current_location == control_room:
            if user_command.endswith('icespell'):
                for item in inventory_dict.keys():
                    if user_command.endswith('icespell'):
                        print('Trolls are imune to icespells')
                    
                        break
                else:
                    print('That did not work.')

            elif invisible == True:
                if user_command.endswith('square'):
                    for item in current_location.usables.keys():
                        if item == 'square':
                            value= current_location.usables.get(item)
                            square_ispressed = True
                            print('You press the ' + value + 'key' + '\n')
                            x = input(colored('The square turns green. Next button please. > ', 'green'))
                            user_command = x.lower()
                            
                            if user_command.startswith('use') and current_location == control_room:
                                if user_command.endswith('triangle'):
                                    for item in current_location.usables.keys():
                                        if item == 'triangle':
                                            value= current_location.usables.get(item)
                                            triangle_ispressed = True
                                            print('You press the ' + value + 'key' + '\n')
                                            x = input(colored('The triangle turns green. Next button please. > ', 'green'))
                                            user_command = x.lower()
                            
                                            if user_command.startswith('use') and current_location == control_room:
                                                if user_command.endswith('circle'):
                                                    for item in current_location.usables.keys():
                                                        if item == 'circle':
                                                            value= current_location.usables.get(item)
                                                            circle_ispressed = True
                                                            print('You press the ' + value + 'key' + '\n')
                                                            print('The square, triangle and circle flash green.')
                                                            print('A symbol of a gate appears just above the buttons. What did you just do?')
                                                            library_gate.description = 'a large open black iron leads into the library.\n' + 'You can tell by the large sign above the gate that says:\n' + '"LIBRARY".'
                                                            library_gate.east = library
                                                            library_gate.directions = 'You can go West and East.'
                                                            library_gate.short_description = 'An open iron gate leading to the library.'
                                                            invisible = False
                                                            print('You hurry away from the controlpanel and remove the cloak.')
                                                            print('As you turn visible again, you see the troll did not even notice.')
                                                            print("You can't breathe in this thing!")
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
                    print('That did not work.')
            
            elif user_command.endswith('square'):
                print('The troll sees you and pushes you back.')
                print('GET AWAY FROM THEM CONTROLS, YA WIMP!!')
                print('As long as he can see you, you can not get close.')
            elif user_command.endswith('triangle'):
                print('The troll sees you and pushes you back.')
                print('GET AWAY FROM THEM CONTROLS, YA WIMP!!')
                print('As long as he can see you, you can not get close.')
            elif user_command.endswith('circle'):
                    print('The troll sees you and pushes you back.')
                    print('GET AWAY FROM THEM CONTROLS, YA WIMP!!')
                    print('As long as he can see you, you can not get close.')

            else:
                ('That does not seem to work.')

        elif user_command == 'take cloak' and current_location == observatory:
            if climbed_beanstalk == False:
                rint('The cloak is way too high. I need something to reach it.')
            else:
                print('You allready have the cloak. Look, it is in')
        
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

                elif user_command.endswith('note') and current_location == hallway3:
                        item = 'note'
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description1 = ''
                        break

                elif user_command.endswith('plantfood') and current_location == garden:
                        item = 'plantfood'
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description1= ''
                        break
                
                elif user_command.endswith('beans') and current_location == garden:
                        item = 'beans'
                        value= current_location.interactible.get(item)
                        inventory_dict[item] = value
                        del current_location.interactible[item]
                        print('You take the ' + item + '\n')
                        current_location.description2= ''
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
            if current_location.inter == True:
                for item in current_location.interactible.keys():
                    if user_command.endswith(item):
                        value= current_location.interactible.get(item)
                        print(value)
                        print('Is in the location.')
                        break
                else:
                    print('You can not examine that.\n')

            elif current_location.usab == True:
                for item in current_location.usables.keys():
                    if user_command.endswith(item):
                        value= current_location.usables.get(item)
                        print(value)
                        print('Is in the location.')
                        break
                else:
                    print('You can not examine that.\n')

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
print('Good to meet you ' + (colored(user_name, 'green') + ', now let us begin.\n'))
intro()
gameloop()
