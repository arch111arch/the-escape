# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from termcolor import colored, cprint
import time

inventory_dict = {}
delay = 1
logo = (colored('THE ESCAPE', 'yellow', attrs=['bold']))
user_command = ''

class Location:
    def __init__(self, description, short_description, new_description, directions):
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


teleportation_chamber = Location('''A vaulted room illuminted by strange glowing 
symbols in the stonewalls\n.
In the center of the room is a pentagram painted on the floor surrounded
by lit white candles.\n
In a black shelf you see a glass vial with a label of a skull.
In a corner stands a red round table.\n
A gold KEY is on the table.''', '''You are in the 
teleportation-chamber.''', '', 'directions')
teleportation_chamber.name = 'Teleportation Chamber'
teleportation_chamber.short_description = 'You are in the teleportation-chamber.'
teleportation_chamber.new_description = '''a vaulted room illuminted by strange glowing 
symbols in the stonewalls\n.
In the center of the room is a pentagram painted on the floor surrounded
by lit white candles.\n
In a corner stands a red round table.'''

teleportation_chamber.directions = 'You can go: East'
teleportation_chamber.interactible = {
  "key": "A small golden key, carved like a dragon.",
  "model": "Mustang",
  "year": 1964
}

teleportation_chamber.usables = {
  "poison": "Glass vial with a dangerous looking green liquid.",
  "gizmo": "use to exit."
}

potions = Location('''five shelves are filled with jars, bottles and strange,
instruments and burning candels.\n
There is bottle with blue liquid on a table.''', 'a dimly lit potions chamber.', 'This is the new description.', 'directions')
potions.directions = 'You can go: East'

control_room = Location('''this bright control-room is allmost entirely filled
 with computerscreens, buttons and levers. 
 In the center is a large controlpanel.\n
 On a coathanger you see a blue and yellow cloak.''', ' a room filled with computers and machines.', 'This is the new description.', 'directions')
control_room.directions = 'You can go: East'

control_room.interactible = {
  "cloak": "A cloak of invisibility!",
  "model": "Mustang",
  "year": 1964
}

hallway = Location('''this hallway continues ends in total darkness.''', ' a dark hallway.', 'This is the new description.', 'directions')
hallway.directions = 'You can go: East'

exit = Location('''EXIT.''', ' the exit.', 'This is the new description.', 'directions')
exit.directions = 'You can go: Exit'


pool = Location('''in front of a wooden platform, a black icy cold pool stretches across the long chamber and 
ends in an identical wooden platform on the other side.''', 'a large black pool, icy cold.', 'This is the new description.', 'directions')
pool.directions = 'You can go: East'

#blocked = Location('you can not go that way.' , 'you can not go that way','This is the new description.')

#teleportation_chamber.north = pool
teleportation_chamber.west = control_room
teleportation_chamber.east = potions
#teleportation_chamber.south = blocked

#pool.north = blocked
#pool.west = blocked
#pool.east = blocked
pool.south = teleportation_chamber

#control_room.north = blocked
#control_room.west = blocked
control_room.east = teleportation_chamber
#control_room.south = blocked

#potions.north = blocked
potions.west = control_room
#potions.east = blocked
#potions.south = blocked


current_location = teleportation_chamber

def intro():
    print('Everything is black.')
    ('\n')
    print('You are in the ' + current_location.name + '. You see ' + current_location.description)
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

    while user_command != 'quit':
       
        print('')
        x = input(colored('What do you do now? > ', 'green'))
        user_command = x.lower()
        loc = current_location
        print('\n')
        #makes sure every input is lowercase to avoid errors.

      

    print('QUITTING GAME')



print('Welcome to the text-adventure ' + logo)
print('')

user_name = input('What is your name, adventurer? > ')
print('') 
print('Good to meet you ' + (colored(user_name, 'green')) 
+ ', now let us begin.\n')

intro()
gameloop()



