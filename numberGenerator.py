import random


def numberGenerator():

    print("\nI am thinking of a 3-digit number. Can you guess what it is?")
    print("Here are some clues:")
    print("When I say:      That means:")
    print("RED              No digit is correct.")
    print("YELLOW           One digit is correct but in the wrong position.")
    print("GREEN            One digit is correct and in the right position.")
    print("You have 10 guesses to get it. Goodluck!")
    print("To quit early, type '0'")

    a = str(random.randint(0,9))
    b = str(random.randint(0,9))
    c = str(random.randint(0,9))
    randNumber = a + b + c
    counter = 1
    play = True

    while play:
        if counter < 11:
            guess = input("\nGuess " + str(counter) + ": \n")
            counter += 1
            if guess == '0':
                break
            elif guess == randNumber:
                print("You got it!")
                playAgain()
                break
            elif guess != randNumber and counter == 11:
                print("You did not correctly guess the number :(")
                print("The correct number was " + randNumber + '.')
            elif guess != randNumber:
                compare(randNumber, guess)
        else:
            playAgain()
            break
                

            
        
def playAgain():
    again = input("Would you like to play again? (yes / no) ")
    if again == "yes":
        numberGenerator()
    elif again == "no":
        print("Thanks for playing!\n")

def compare(randNumber, guess):
    i = 0
    j = 0

    for x in guess:
        if i < 3:
            if x == randNumber[i]:
                print("GREEN")
                i += 1
            elif x in randNumber:
                print("YELLOW")
                i += 1
            else:
                j += 1
                i += 1
                if j == 3:
                    print("RED")
        else:
            break

numberGenerator()