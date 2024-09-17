#Leap Year task (3)

year= int(input("Enter a year:"))

if (year%400==0 and year%100==0) or (year%4==0 and year%100!=0):
    print(year,"It is a leap year")
else:
    print(year,"It is not a leap year")    



year = int(input("Enter a year:"))

if (year%400==0 and year%100==0):
    print(year,"It is a leap year")
elif (year%4==0 and year%100!=0):
    print(year,"It is a leap year")
else:
    print(year,"it is not a leap year")


year = int(input("Enter a year:"))

if (year%400==0):
    print(year,"It is a leap year")
elif (year%4==0 ):
    print(year,"It is a leap year")
elif(year%100==0):
    print(year,"It is a leap year")
else:
    print(year,"it is not a leap year")


#-----------------------------------------------------------------------------------------------------------------------------
# simple calculator task (2)

num1 = float(input("Enter a first number"))
oper = (input("enter a operator (+,-,*,/,%)"))
num2 = float(input("Enter a second number"))

if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    print(num1/num2)
elif oper == "%":
    print(num1/num2*100)
else:
    print("enter a wrong operator")


num1 = int(input("Enter a first number"))
oper = (input("enter a operator (+,-,*,/,%)"))
num2 = int(input("Enter a second number"))

if oper == "+":
    print(num1+num2)   
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    if num2!=0:
        print(num1/num2)
    else:
        print("zero is not allowed")
elif oper == "%":
    print(num1/num2*100)
else:
    print("enter a wrong operator")

#---------------------------------------------------------------------------------------------------------------------
#rock paper scissors (2)
user1 = input("What isyour name:")
user2 = input("And Your Name?:")
print("Welcome to the Game")
print("Let's Start The Game")
user1 = str(input("enter a  first player:"))
user2 = str(input("enter a second player:"))
if user1=="rock" and user2 =="paper" or user1 == "paper" and user2=="sissors":
    print("user 2 winner")
elif user1=="paper" and user2=="rock" or user1 =="sissors"and user2=="paper":
    print("user1 winner")
elif user1=="sissors" and user2=="rock" :
    print("user2 winner")
elif user1=="rock" and user2=="sissors":
    print("user1 winner")
elif user1=="rock"and user2=="rock" or user1=="sissors" and user2=="sissors" or user1=="paper"and user2=="paper":
    print("Match Tied")
else:
    print("wrong enter str")

user1 = str(input("what is your name"))
user2 = str(input("And your name?:"))
print(user1,"select a sissors,rock,paper")
choice1 = input()
print(user2,"select a sissors,rock,paper")
choice2 = input()
if choice1=="rock" and choice2 =="paper" or choice1 == "paper" and choice2=="sissors":
    print("user 2 winner")
elif choice1=="paper" and choice2=="rock" or choice1 =="sissors"and choice2=="paper":
    print("user1 winner")
elif choice2=="sissors" and choice2=="rock" :
    print("user2 winner")
elif choice1=="rock" and choice2=="sissors":
    print("user1 winner")
elif "choice1==choice2":
    print("match tied")
else:
    print("wrong enter str")

#----------------------------------------------------------------------------------------------------------
#Word guessing game (1)

import random

words = ["python","java", "php", "javascript", "shubham"]
def word_guessing_game():
 print("Welcome to the Word Guessing Game!")
    
    
player_name = input("Enter your name: ")
print(f"Hello, {player_name}! Let's start the game.")
print("hello ", player_name , "! Lets start ")
    
chosen_word = random.choice(words)

    
guess = input("Guess the word: ")

print(chosen_word)
    
if guess == chosen_word:
    print(f"Congratulations, {player_name} You guessed the word correctly: (chosen_word)")
else:
    print("Sorry, that was incorrect. The game will now close.")
        
print(word_guessing_game())

#--------------------------------------------------------------------------------------------------------------------------
#Quiz Competition Game (1)

print("Welcome To the Quiz Competition")

a = (str(input("Enter Your Name")))
print(a)
b = (str(input("Enter your Email Id")))
print(b)

print("Hello",a,"Are You Ready?")
d = str(input("Enter Your Ans"))

if d == "yes":
    print("Lets Start The Game")
elif d == "no":
    print("Then Not Start The Quiz Compitetion")
    exit()
else:
    print("Invalid Ans")
    exit() 

score = 0

print("1. Which planet is known as the Red Planet?")    
print("A) Venus \nB) Earth \nC) Jupiter \nD) Mars")
Ans = str(input("Enter Your Option"))
print(Ans)
if Ans == "D":
    print("Congratulation",a,"Your Ans is correct ")
    score +=5
else:
    print("Sorry",a,"Your Ans is wrong... D) is correct Ans")
    score -=2

print("2. What is the largest mammal in the world?")
print("A)Elephant \nB) Blue Whale \nC) Great White Shark \nD) Giraffe")
Ans = str(input("Enter Your Option"))
print(Ans)
if Ans == "B":
    print("Congratulation",a,"Your Ans is correct ")
    score +=5
else:
    print("Sorry",a,"Your Ans is wrong... B) is correct Ans")
    score -=2

print("3. What is the capital city of Japan?")
print("A) Seoul \nB) Beijing \nC) Tokyo \nD) Bangkok")
Ans = str(input("Enter Your Option"))
print(Ans)
if Ans == "C":
    print("Congratulation",a,"Your Ans is correct ")
    score +=5
else:
    print("Sorry",a,"Your Ans is wrong... C) is correct Ans")
    score -=2

print("4. What is the chemical symbol for water?")
print("A) H2O \nB) O2 \nC) CO2 \nD) NaCl")
Ans = str(input("Enter Your Option"))
print(Ans)
if Ans == "A":
    print("Congratulation",a,"Your Ans is correct ")
    score +=5
else:
    print("Sorry",a,"Your Ans is wrong... A) is correct Ans")
    score -=2

print("5. What is the Capital city of Maharashtra?")
print("A) Delhi \nB) Mumbai \nC) Nagpur \nD) Pune")
Ans = str(input("Enter Your Option"))
print(Ans)
if Ans == "B":
    print("Congratulation",a,"Your Ans is correct ")
    score +=5
else:
    print("Sorry",a,"Your Ans is wrong... B) is correct Ans") 
    score -=2  

print("6. Full Form Of ML?")
print("A) Model Learning \nB) Manage Learner \nC) Machine Learning \nD) None Of the above")
Ans = str(input("Enter Your Option"))
print(Ans)
if Ans == "C":
    print("Congratulation",a,"Your Ans is correct ")
    score +=5
else:
    print("Sorry",a,"Your Ans is wrong... C) is correct Ans")
    score -=2

print("Quiz Completed !" "\n Your Final score is ",score)

if score >=25:
    print("Outstanding")
elif score >=21:
    print("Excellent")
elif score >=17:
    print("Very Good")
elif score >=13:
    print("Good")
elif score >=9:
    print("Average")
else:
    ("Better Than Next Time")

print("Thank You")

#---------------------------------------------------------------------------------------------------------------
# Pizza Sale Task (1)

pizza_prices = {
    'small': 80,
    'medium': 100,
    'large': 120
}

topping_price = 25

print("Welcome to the Pizza Shop!")
size = input("Choose pizza size (small, medium, large): ")

if size not in pizza_prices:
    print("Invalid size, please choose small, medium, or large.")
else:
    num_pizzas = int(input("How many pizzas would you like to order? "))

    extra_toppings = input("Would you like extra toppings? (yes or no): ")
    
    total_cost = num_pizzas * pizza_prices[size]
    
    if extra_toppings == 'yes':
        num_toppings = int(input("How many extra toppings would you like? "))
        total_cost += num_toppings * topping_price * num_pizzas
    
    print(f"\nYour order summary:")
    print(f"Size of pizza: {size.capitalize()}")
    print(f"Number of pizzas: {num_pizzas}")
    print(f"Extra toppings: {'Yes' if extra_toppings == 'yes' else 'No'}")
    print(f"Total cost: ${total_cost:.2f}")
