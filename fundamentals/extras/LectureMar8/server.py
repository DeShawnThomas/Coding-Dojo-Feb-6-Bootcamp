from assets.jokes import jokes_list
from assets.quotes import quotes_list
import time
import random 

# time.sleep(5)
# print(jokes_list[0])

def jokeBot():
    print('Do you want to hear a joke? Type "y" or "n"?')
    user_input = input()
    if user_input == "y":
        this_joke = random.choice(jokes_list)
        print("...Okay lemme think")
        time.sleep(2)
        print(this_joke["setup"])
        time.sleep(5)
        print(this_joke["punchline"])
    elif user_input == "n":
        print("Awww... okay :/")
    else:
        print("I'm not sure what you said...")

jokeBot()