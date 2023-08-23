import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'json/username.json'
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a username."""
    username = input("What is Your name? ")
    filename = 'json/username.json'
    with open(filename,'w') as file_obj:
        json.dump(username, file_obj)
        return username

def greet_user():
    """Greet username by name"""
    username = get_stored_username()
    check_username = input(f"Is '{username.title()}' correct username? (enter y for yes and n for no) ")
    if check_username == 'y':
        print(f"Welcome back, {username} !")
        
    else:
        username = get_new_username()
        print(f"We will remember you wwhen you come back {username}.")
            
        
greet_user()
        