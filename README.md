![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Battleships

Battleships is a Python terminal game, deployed on Heroku.

Users can try to beat the computer by hitting all the pcs battleships before the computer finds theirs. Each battleship occupies one square on the board.

# How to play

Battleships is a strategy type guessing game for two players. Within this game, it is played on a grid where the user has a board and the pc has a board. Locations of the ships of the pc board are concealed from the user. All ships are positioned randomly. 

The user can see where its ships are placed indicated by an '0' but cannot see where the computers ships are. Guesses are marked with 'G' and hits are indicated by 'X'.

The pc and user take turns to try there shot at sinking each others ships. The winner is the player who successfully sinks all of their opponet's battleships first. 

# Features

Random board generation:
- Ships are randomly placed on both the player and computer boards
- The player cannot see where the computer's ships are
- user vs the pc
- Accepts user input
- Maintains scores

Input validation and error-checking:
- You cannot enter coordinates outsdie the size of the grid
- You must enter integers
- You cannot enter the same guess twice
- Data maintained in class instances

# Future Features

Allow user to select the board size and number of ships
Allow user to position the ships themselves
Have ships larger than 1x1

# Data Model

I decided to use Board class as my model. The game creates two instances of the Board class to hold the user's and the pc's board. 

The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board, and details such as the board type (user's board or pc) and the user's name. 


# Testing

I have manually tested this project by doing the following:

- Passed my project through PEP8 linter and confirmed there were no issues. 
- Tested my project by giving it invaild inputs: letters when numbers were expected, guesses outside the range of my board, same input twice. 
- Tested it in both my local terminal and the Code Institute Heroku terminal 

# Bugs

## Solved Bugs
- 

- No bugs remaining

## Validator Testing

- PEP8online.com:
No errors were returned.

## Deployment 

This project was deployed using Code Institute's mock terminal for Heroku. Due to a security breach I was not able to deploy via the dashboard - I deployed fully through the terminal in my workspace. Steps are below.  

Steps:
- I ran the command heroku login -i to prompt login in the terminal of my workspace. 
- I then ran the command heroku create bship4 to create a new app called 'bship4.'
- This created a new Heroku app and linked it to my Gitpod terminal. 
- I was then able to access my app via the Heroku dashboard and set up my config vars and building packs. 
- I set the buildpacks to Python and NodeJS in that order.
- I added the config vars - key - PORT , value - 8000 - as instructed. 
- I ran the command git push heroku main to update my app as I continued to work on it in my workspcae. 

## Credits
- Code Institue for the deloyment terminal.
- My Mentor for his much valued time and help with my project. 
- Code Insitute Tutor Support for help with my project. 
- Slackover flow
