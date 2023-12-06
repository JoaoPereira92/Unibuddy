def get_user():
    """Function getting user name."""
    username = input("Whats your name?\n")
    while username.isalpha() is False:
        print("I don't recognize numbers or symbols as a name.")
        username = input("What's your name?\n")
    return username



def get_colour():
    """Function getting user's favorite colour."""
    user_colour = input("What's your favorite color?\n")
    return user_colour



def get_age(username):
    """Function getting user's age."""
    user_age = input(f"How old are you {username}?\n")
    
    while not user_age.isdigit():
        user_age = input("Please introduce a valid number! ")
    
    while int(user_age) > 120 or int(user_age) < 0:
        user_age = input(f"Please {username}, tell me your real age: ")

    return user_age
    
    

    
    