import random

print("Welcome to Nanda's Number Guessing game")

number = random.randint(1,9)

chances = 0

print("Guess a number(between 1-9):")

while chances < 5:
 guess=="answermode":
	guess=int(input("Enter your guess:-"))

if guess == number:
           print("CONGRATULATIONS YOU WON!")
     
           break 

elif guess < number:
	print("Your guess was too low.Guess a number higher than",guess)

    else guess > number:
    print("Your guess was too high.Guess a number smaller than",guess)
	
chances += 1

if not chances < 5:
    print("You Lose!The number is ",number) 

