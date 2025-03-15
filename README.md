# Dice Rolling Game

## Description
This is a simple Dice Rolling Game implemented in Python. The game allows the user to roll a specified number of dice multiple times based on their input. The game ensures user input validation and provides a friendly interface for playing.

## Features
- User can decide whether to roll the dice (Yes/No).
- Generates random numbers (1-6) representing dice rolls.
- Allows the user to roll multiple dice per turn.
- Limits the number of rolls per game to prevent excessive play.
- Provides feedback for invalid inputs.
- Displays the total number of rolls at the end of the game.

## How to Play
1. Run the script in a Python environment.
2. The program will ask if you want to roll the dice. Enter "Yes" or "No".
3. If "Yes", enter the number of dice you want to roll (1-5).
4. The program will generate random numbers for each die.
5. The game allows a maximum of 5 rolls per session.
6. If "No", the game will terminate with a thank-you message.
7. If an invalid input is entered, the program will prompt for a correct response.

## Requirements
- Python 3.x

## Installation
1. Download or clone this repository.
2. Ensure Python is installed on your system.
3. Run the script using the command:
   ```bash
   python dice_rolling_game.py
   ```

## Example Gameplay
```
Roll the dice? (Yes/No): Yes
Enter the number of dice to roll: 2
Roll 1: [3, 5]

Roll the dice? (Yes/No): Yes
Enter the number of dice to roll: 1
Roll 2: [6]

Roll the dice? (Yes/No): No
Thanks for playing! You rolled the dice 2 times.
```

## Notes
- The game ensures input validation to prevent crashes.
- Maximum dice rolls are limited to 5 in one session.
- Entering invalid choices will prompt the user to enter valid input.

## License
This project is open-source and free to use.

## Author
Developed by Mrunal Patange.

