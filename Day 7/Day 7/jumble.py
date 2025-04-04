

'''
    Jumbled Word: "otpcomure"
    Your Guess: "computer"
    ✅ Correct! 


1. Based on the above code   

   Give players two attempts
   If the player guesses in the first attempt give 2 points, in the second attempt 1 points, otherwise 0
   Allow players to get hints/clues if they fail to guess in the first attempt
   Give the result based on total points, total first attempts, total second attempts
   Use appropriate unicode charecters

   Example: 'alepp'
             Can you guess? ape 
             CLUE: 'This is a fruit'
             Take a second guess? apple
             ✅ Correct! 

             ...

             Total          = 18
             First          = 5
             Second         = 8
             Overall        = B+

   Challenge: Keep the hints in the file. How to read the the words and hints from a file and integrate it
            Come up with a logic to display the result'''

import random

# function to jumble the word

def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)


# Welcome message

print("\n")
print("Welcome to the WORD JUMBLE GAME")
print("-" * 80)

print("The computer presents a jumbled word")
print("You need to guess it. For every correct guess")
print("you will be offered a point")
print("-" * 80)

# Get the words and process it 
path = r"C:\Users\265148\Desktop\New folder\Day 7\words.txt"
hints_path = r"C:\Users\265148\Desktop\New folder\Day 7\hint.txt"
f = open(path)
content = f.read()
f.close()

h = open(hints_path, 'r')
hints = h.read().splitlines()
h.close()

content = content.split(', ')

fruits = content[:5]
veg = content[5:]

fruits_h = hints[0]
veg_h = hints[1]

print(fruits)
print(veg)
# print("INFO content -> ", content)

points = 0
second_attempt = 0
# for every word in list of words
random.shuffle(content)

total_points = 0
total_first_attempts = 0
total_second_attempts = 0

for word in content:

    #print("\n")

    # jumble the word
    jumbled_word = jumble(word)

    # show to the user
    print(jumbled_word)

    # ask user input
    user_word = input("Can you guess -> ")

    # compare user input and update points
  
    if user_word == word:
        print(f"Correct! You guessed it on the first attempt.\n")
        print("-" * 80)
        total_points += 2
        total_first_attempts += 1 

    else:
        print("Incorrect!")
            # Provide a hint and give a second attempt
            #hint = give_hint(word)
            #print(f"Hint: {hint}")
        if word in fruits:
            print(f"Hint: {fruits_h}")
        else:
            print(f"Hint: {veg_h}")

            # Second attempt
        user_word = input("Attempt 2 -> ").lower()
        if user_word == word:
            total_points += 1
            total_second_attempts += 1
            print("Correct! You guessed it on the second attempt.\n")
            print("-" * 80)
        else:
            print(f"Incorrect! The correct word was: {word}\n")
            print("-" * 80)

    # compare user input and update points
    
    

# show the results

print("-" * 80)

'''if(total_points > 6):
    print("You have played well")
else:
    print("You need to improve on your vocabulary")'''


print(f"The total points scored {total_points}")
print(f"items guessed in first attepmt{total_first_attempts}")
print(f"items guessed in first attepmt{total_second_attempts}")
 
if (total_points>15 and (total_first_attempts ==9 and total_second_attempts==0)):
    print("O-outstanding")
elif(total_points>=15 and (total_first_attempts >=6 and total_second_attempts<=3)):
    print("A-Very good")
elif(total_points>=12 and (total_first_attempts >=4 and total_second_attempts<=5)):
    print("B-good")
elif(total_points>=8 and (total_first_attempts >=2 and total_second_attempts<=7)):
    print("c-Average")
else:
    print("please improve your vocabulaby")