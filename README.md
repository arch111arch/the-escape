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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


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
