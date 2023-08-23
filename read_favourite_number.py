import json 

filename = 'json/favourite_number.json'

try:
    with open(filename) as file_obj:
        number = json.load(file_obj)
except FileNotFoundError:
    print(f"File {filename} does not exist.")
else:
    print(f"Your favourite number is {number}")