
"""
Random Number
"""

import random

def main():
    print("Welcome to Camel! \nYou have stolen a camel to make your way across the great Mobi desert. \nThe natives want their camel back and are chasing you down! \nSurvive your desert trek and out run the natives.")
    done = False
    miles_traveled = 20
    thirst = 0
    camel_tiredness = 0
    canteen_drinks = 3
    native = 10
    distance_btw_you_native = miles_traveled - native

    while done == False:

        print("A. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop for the night. "
              "\nE. Status check. \nQ. Quit.")
        user_Choice = input("What is your choice?  ")
        if user_Choice.upper() == "Q":
            done = True
            print("You have quit the game")
        elif user_Choice.upper() == "E":
            print("Miles traveled: ", miles_traveled, "\nDrinks in canteen: ", canteen_drinks, " \nThe natives are ", distance_btw_you_native,  "miles behind you.")
        elif user_Choice.upper() == "D":
            camel_tiredness = 0
            native = native + random.randrange(7, 14)
            distance_btw_you_native = miles_traveled - native
            print("The camel is happy")

        elif user_Choice.upper() == "C":
            miles_traveled = miles_traveled + random.randrange(10, 20)
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + random.randrange(1, 3)
            native = native + random.randrange(7, 14)
            distance_btw_you_native = miles_traveled - native
            print("You have traveled", miles_traveled)

        elif user_Choice.upper() == "B":
            miles_traveled = miles_traveled + random.randrange(5, 12)
            thirst = thirst + 1
            native = native + random.randrange(7, 14)
            distance_btw_you_native = miles_traveled - native
            print("You have traveled", miles_traveled)

        elif user_Choice.upper() == "A":
            if canteen_drinks > 0:
                canteen_drinks = canteen_drinks - 1
                thirst = 0
            else:
                print("No more drink left in the canteen")
        if thirst > 4:
            print("You are thirsty")

        if thirst > 6:
            print("You died of thirst")
            done = True
        if camel_tiredness > 5:
            print("Your camel is getting tired")
        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True

        if native >= miles_traveled:
            print("The natives caught the player")
            done = True
        if miles_traveled - native < 15:
            print("The natives are getting close!")

        if miles_traveled >= 200:
            print("You have won the game")
            done = True





main()