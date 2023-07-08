# The Escape

The Escape is a textbased adventure like the games of old where the user types commands to interact with the program. The object is to escape from the wizards lair.

## Features 

In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### Existing Features

- __Interface__

  - The interface allways gives a description of the current location and the directions that the player can go.
  - New text is presented on a new line to not crowd the screen.
  - Colors are used sparingly, only to highlight a misstake or the available directions for example. 


- __Inventory__

  - The inventory shows only items if the player has taken any. IF not is´t shows that it is empty.
  - When the player types get and an item, that is added to a dictionaty.


- __Error Handling__

  - Since items were often None, those exceptions were handled using try except.


### Features Left to Implement

- Enemy-system, health and a combat-system.

## Testing 

I ran the game several times and fixed many bugs along the way dealing with excetions and intendation-errors.


### Validator Testing 
- https://pep8ci.herokuapp.com/ Validator has unfortunately found many errors. I will deal with them after feedback.


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 


## Credits 

Several problems, especially with error-handling and how to deal with exceptions was found on various forums like:
- https://www.positioniseverything.net/nonetype-object-has-no-attribute/
- https://www.w3schools.com/python/python_try_except.asp
- And videos on youtube by Neal Holtshultse dealing with classes.
- 
### Content 

- To color text teh library termcolor was imported
- to use timed events, the libraray time was imported

### Media

- No media used for the project.
