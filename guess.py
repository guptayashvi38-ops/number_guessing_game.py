import random

comp=random.randint(1,10)
attempts=3

while attempts>0:
    guess=int(input("Enter a number:"))
    
    if guess==comp:
        print("Bingo! You found it !!")
        break

    elif guess>comp:
        print("Too High")
    else:
        print("Too low")

    attempts-=1
    print("Wrong! Your attempts left:",attempts)


if attempts==0:
    print("The correct number was:",comp)
