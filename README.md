![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Battleships

Battleships is a Python terminal game, deployed on Heroku.

Users can try to beat the computer by hitting all the pcs battleships before the computer finds theirs. Each battleship occupies one square on the board.

## How to play

Battleships is a strategy type guessing game for two players. Within this game, it is played on a grid where the user has a board and the pc has a board. Locations of the ships of the pc board are concealed from the user. All ships are positioned randomly. 

The user can see where its ships are placed indicated by an '0' but cannot see where the computers ships are. Guesses are marked with 'G' and hits are indicated by 'X'.

The pc and user take turns to try there shot at sinking each others ships. The winner is the player who successfully sinks all of their opponet's battleships first. 

## Features

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

## Future Features

Allow user to select the board size and number of ships
Allow user to position the ships themselves
Have ships larger than 1x1

## Data Model

I decided to use Board class as my model. The game creates two instances of the Board class to hold the user's and the pc's board. 

The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board, and details such as the board type (user's board or pc) and the user's name. 


## Testing

## Bugs

## Deployment

## Credits


## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!