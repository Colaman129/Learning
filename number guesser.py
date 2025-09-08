import random
num2 = int(input("Guess the number: "))
num = random.randint(1, 100)

while not num2 == num:

    if num2 == num:
        print("Correct")
    elif num2 > num:
        print("Less")
    elif num2 < num:
        print("More")
    num2 = int(input("Guess the number: "))
print("You guessed it")