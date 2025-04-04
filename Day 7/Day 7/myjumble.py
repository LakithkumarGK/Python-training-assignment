'''
import random

path = r"C:\Users\265148\Desktop\New folder\Day 7\words.txt"
f = open(path)
content = f.read()
f.close()

content = content.split(', ')
print("Content", content)

def jumble(word):
    temp = list(word)
    random.shuffle(temp)
    return ''.join(temp)

point = 0

for word in content:
    jumble_word = jumble(word)

    print("Can you guess the jumbled word")
    print(jumble_word)

    user_word = input("->")

    if user_word == word:
        point += 10
        print("Correct \U00002705 \n")
    else:
        print("Incorrect\n")
print("-"*80)
if point < 30:
    print("Please work hard")
else:
    print("Good!!!!")
print("-"*80)'''
'''---------------------------------------------------------------------------------------------
import random

# Path to your file containing the words
path = r"C:\Users\265148\Desktop\New folder\Day 7\words.txt"

# Reading the file content
with open(path) as f:
    content = f.read()

# Split the content by comma and space (', ')
content = content.split(', ')
print("Content:", content)

# Function to jumble the word
def jumble(word):
    temp = list(word)
    random.shuffle(temp)
    return ''.join(temp)

# Initialize the counters for points and attempts
total_points = 0
total_first_attempts = 0
total_second_attempts = 0

# Function to provide a hint (reveals the first letter)
def give_hint(word):
    return f"The word starts with: {word[0].upper()}"

# Game loop
for word in content:
    jumble_word = jumble(word)  # Get the jumbled word
    print("Can you guess the jumbled word?")
    print(jumble_word)

    # First attempt
    user_word = input("Attempt 1 -> ").lower()
    if user_word == word:
        total_points += 2
        total_first_attempts += 1
        print("Correct! You guessed it on the first attempt.\n")
    else:
        print("Incorrect!")
        
        # Provide a hint and give a second attempt
        hint = give_hint(word)
        print(f"Hint: {hint}")

        # Second attempt
        user_word = input("Attempt 2 -> ").lower()
        if user_word == word:
            total_points += 1
            total_second_attempts += 1
            print("Correct! You guessed it on the second attempt.\n")
        else:
            print(f"Incorrect! The correct word was: {word}\n")

# Display the final results
print("-" * 80)
print(f"Total Points: {total_points} ")
print(f"Total First Attempts: {total_first_attempts} ")
print(f"Total Second Attempts: {total_second_attempts} ")

# Display a final message based on the score
if total_points < 30:
    print("Please work harder! ")
else:
    print("Good job! Keep it up! ")
print("-" * 80)'''


