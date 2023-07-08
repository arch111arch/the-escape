# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from termcolor import colored, cprint
import time

inventory_dict = {}
delay = 1
logo = (colored('THE ESCAPE', 'yellow', attrs=['bold']))
user_command = ''





print('Welcome to the text-adventure ' + logo)
print('')

user_name = input('What is your name, adventurer? > ')
print('') 
print('Good to meet you ' + (colored(user_name, 'green')) 
+ ', now let us begin.\n')




