#diceRollingGame
# Ask: User Input (Yes or No )
# If user Enter Yes Generate 2 random numbers 
# If user Enter No then print "Thank You"
#Terminate
#Else (Invalid Input if user input does not matched with out condition)


import random

# Counter to track number of rolls
roll_count = 0  

while True:
    choice = input('Roll the dice? (Yes/No ): ').lower()
    
    if choice == 'yes':
        try:
            num_dice = int(input('Enter the number of dice to roll: '))
            if num_dice < 1:
                print("Please enter a valid Integer number of dice (at least 1).")
                continue
            
            # Increment roll count
            roll_count += 1 
            #The randint() method returns an integer number selected element from the specified range.
            ##Note: This method is an alias for randrange(start, stop+1). 
            rolls = [random.randint(1, 6) for _ in range(num_dice)]
            print(f'Roll {roll_count}: {rolls}')
        
        except ValueError:
            print("Invalid input! Please enter a valid Integer number.")
    
    elif choice == 'no':
        print(f'Thanks for playing! You rolled the dice {roll_count} times.')
        break
    
    else:
        print('Invalid choice! Please enter Yes or No.')













































import random
# Get user input and ensure it's within the limit
totalCount = int(input("How many times do you want to roll the dice? (Max: 5) "))

if totalCount > 5:
    print("Sorry, you can roll a dice only 5 times in one game.")
    totalCount = 5

print(f"You can roll the dice {totalCount} times.")

#How many Dice Roll 
max_dice = 5
num_dice = int(input("How many dice do you want to roll? (1-5): "))

if num_dice < 1 or num_dice > max_dice:
    print("Invalid number of dice. Please choose between 1 and 5.")
    num_dice = max_dice

print(f"You will roll {num_dice} dice each turn.")

# Initialize roll counter
roll_count = 0

while roll_count < totalCount:
    #The strip() method removes any leading, and trailing whitespaces.7

    choice = input("Roll the dice? (Yes / No): ").strip().lower()

    if choice == 'yes':
        roll_count += 1
        # The randint() method returns an integer number selected element from the specified range.

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Roll {roll_count}: ({die1}, {die2})")

        # If user reaches max rolls, end the game
        if roll_count == totalCount:
            print("You have reached the maximum number of rolls.")
            break

    elif choice == 'no':
        print("Thanks for playing!")
        break

    else:
        print("Invalid Choice. Please enter 'Yes' or 'No'.")

print("Game Over!")

 
       