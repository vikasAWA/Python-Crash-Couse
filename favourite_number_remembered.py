import json

filename = 'json/favourite_number.json'

try:
    with open(filename) as file_obj:
        favourite_number = json.load(file_obj)
except FileNotFoundError:
    favourite_number = input("What is your favourite number? ")
    with open(filename, 'w') as file_obj:
        json.dump(favourite_number, file_obj)
else:
    print(f"I know your favourite number, your favourite number is {favourite_number}")

