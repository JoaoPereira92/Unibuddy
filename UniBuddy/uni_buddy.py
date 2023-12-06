import user_inputs as user
from Data import colours, questions, answers

print("Hello and Welcome to our University, I'm UniBuddy and I'm here to help you!")

# Get user age.
username = user.get_user()
print(f"\nHello {username}! Nice to meet you!")


# Get user favorite colour and see if it's in the dict of colours.
user_colour = user.get_colour().lower()

# Loop till the user chooses one colour from the dict of colours.
while user_colour.lower() not in colours:
    print("I'm sorry I'm afraid i don't recognize that color!\n")
    print(f"I might have a thing or two to say about {', '.join(colours)}!\n")
    user_colour = user.get_colour().lower()

print(colours[user_colour])

# Get user age and print an apropriate message according to his age.
user_age = int(user.get_age(username))

if user_age <= 16 :
    print(f"At the age of {user_age} and already speaking with me? Congratulations!\n")

elif user_age <= 20 :
    print("Welcome to our University! Hope you enjoy your stay!\n")

elif user_age <= 100 :
    print("It's never too late to learn with us, Welcome aboard!\n")

elif user_age >= 100 :
    print(f"Congratulations on reaching {user_age}! PS: I don't believe you!\n")

################################# Display menu #################################

USER_ANSWER = 0


while USER_ANSWER != 6:
    print("Which questions would you like to ask me?:")

    try:
        for key, value in questions.items():
            print(key, ".", value)
        USER_ANSWER = int(input())
        if USER_ANSWER == 6:
            print(answers[USER_ANSWER]+"\n")
            break
        print(answers[USER_ANSWER]+"\n")

        y_n = input("Would you like to ask more questions? (y/n) \n")

        while y_n.lower() not in ["y" , "x"]:
            if y_n.lower() == "y":
                break
            if y_n.lower() == "n":
                USER_ANSWER = 6
                print(answers[6])
                break
            print("Please enter 'y' or 'n': ")

    except ValueError:
        print("Please choose a number from the list of questions. (1-6)\n")
    except KeyError:
        print("Please choose a number from 1-6.")