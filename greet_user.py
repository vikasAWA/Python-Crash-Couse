import json

def greet_user():
    filename = 'json/username.json'
    
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print(f"We will remember you, when you come back, {filename}")
    else:
        print(f"Welcome, {username} !")
            

greet_user()